import sqlite3
import json
from datetime import datetime
from pathlib import Path

class AuditLogger:
    """Audit logging system for tracking all system activity"""
    
    def __init__(self, db_path="logs/audit.db"):
        """Initialize the audit logger"""
        self.db_path = Path(db_path)
        
        # Create logs directory
        self.db_path.parent.mkdir(exist_ok=True)
        
        # Initialize database
        self._initialize_database()
        
        print(f"✅ Audit Logger initialized at {db_path}")
    
    def _initialize_database(self):
        """Create database tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Query logs table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS query_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    sources TEXT,
                    chunks_used INTEGER,
                    model_used TEXT,
                    user_session TEXT,
                    response_time REAL
                )
            """)
            
            # Flagged responses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS flagged_responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    question TEXT NOT NULL,
                    answer TEXT,
                    flag_type TEXT NOT NULL,
                    reason TEXT,
                    user_session TEXT,
                    status TEXT DEFAULT 'open'
                )
            """)
            
            # Wizard logs table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS wizard_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    wizard_type TEXT NOT NULL,
                    data TEXT,
                    checklist TEXT,
                    user_session TEXT,
                    completion_time REAL
                )
            """)
            
            conn.commit()
    
    def log_query(self, question, answer, sources=None, chunks_used=0, model_used="unknown", user_session="anonymous"):
        """Log a question and answer"""
        timestamp = datetime.now().isoformat()
        sources_json = json.dumps(sources) if sources else "[]"
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO query_logs 
                    (timestamp, question, answer, sources, chunks_used, model_used, user_session)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (timestamp, question, answer, sources_json, chunks_used, model_used, user_session))
                conn.commit()
                
        except Exception as e:
            print(f"Error logging query: {e}")
    
    def flag_response(self, question, flag_type="negative", reason="", answer="", user_session="anonymous"):
        """Record flagged response"""
        timestamp = datetime.now().isoformat()
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO flagged_responses
                    (timestamp, question, answer, flag_type, reason, user_session)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (timestamp, question, answer, flag_type, reason, user_session))
                conn.commit()
                
        except Exception as e:
            print(f"Error flagging response: {e}")
    
    def log_wizard_completion(self, wizard_type, data=None, checklist=None, user_session="anonymous"):
        """Log wizard completion"""
        timestamp = datetime.now().isoformat()
        data_json = json.dumps(data) if data else "{}"
        checklist_json = json.dumps(checklist) if checklist else "[]"
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO wizard_logs
                    (timestamp, wizard_type, data, checklist, user_session)
                    VALUES (?, ?, ?, ?, ?)
                """, (timestamp, wizard_type, data_json, checklist_json, user_session))
                conn.commit()
                
        except Exception as e:
            print(f"Error logging wizard completion: {e}")
    
    def get_recent_queries(self, limit=10):
        """Get recent queries"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT timestamp, question, answer, chunks_used, model_used
                    FROM query_logs
                    ORDER BY timestamp DESC
                    LIMIT ?
                """, (limit,))
                
                rows = cursor.fetchall()
                
                queries = []
                for row in rows:
                    queries.append({
                        'timestamp': row[0],
                        'question': row[1],
                        'answer': row[2],
                        'chunks_used': row[3],
                        'model_used': row[4],
                        'sources_count': row[3]
                    })
                
                return queries
                
        except Exception as e:
            print(f"Error getting recent queries: {e}")
            return []
    
    def get_flagged_responses(self, status="open"):
        """Get flagged responses"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT timestamp, question, answer, flag_type, reason
                    FROM flagged_responses
                    WHERE status = ?
                    ORDER BY timestamp DESC
                """, (status,))
                
                rows = cursor.fetchall()
                
                flagged = []
                for row in rows:
                    flagged.append({
                        'timestamp': row[0],
                        'question': row[1],
                        'answer': row[2],
                        'flag_type': row[3],
                        'reason': row[4]
                    })
                
                return flagged
                
        except Exception as e:
            print(f"Error getting flagged responses: {e}")
            return []
    
    def get_usage_stats(self, days=7):
        """Get usage statistics"""
        try:
            from datetime import timedelta
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Count queries
                cursor.execute("""
                    SELECT COUNT(*) FROM query_logs 
                    WHERE timestamp >= ?
                """, (cutoff_date,))
                total_queries = cursor.fetchone()[0]
                
                # Count flagged
                cursor.execute("""
                    SELECT COUNT(*) FROM flagged_responses 
                    WHERE timestamp >= ?
                """, (cutoff_date,))
                flagged_count = cursor.fetchone()[0]
                
                # Count wizards
                cursor.execute("""
                    SELECT COUNT(*) FROM wizard_logs 
                    WHERE timestamp >= ?
                """, (cutoff_date,))
                wizard_completions = cursor.fetchone()[0]
                
                return {
                    'total_queries': total_queries,
                    'flagged_responses': flagged_count,
                    'wizard_completions': wizard_completions,
                    'satisfaction_rate': max(0, 100 - (flagged_count * 100 / max(total_queries, 1)))
                }
                
        except Exception as e:
            print(f"Error getting usage stats: {e}")
            return {
                'total_queries': 0,
                'flagged_responses': 0,
                'wizard_completions': 0,
                'satisfaction_rate': 0
            }
