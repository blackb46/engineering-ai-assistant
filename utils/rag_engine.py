import os
import chromadb
from pathlib import Path
import streamlit as st

class RAGEngine:
    """RAG Engine for question answering using the engineering manual"""
    
    def __init__(self):
        """Initialize the RAG engine"""
        self.client = None
        self.collections = {}
        self.claude_client = None
        self.is_initialized = False
        
        try:
            self._initialize()
        except Exception as e:
            print(f"Warning: RAG Engine initialization failed: {e}")
    
    def _initialize(self):
        """Set up all components"""
        # Connect to vector database
        vectorstore_path = Path("vectorstore")
        if not vectorstore_path.exists():
            raise Exception("Vector database not found. Please run the development notebook first.")
        
        self.client = chromadb.PersistentClient(path=str(vectorstore_path))
        
        # Load collections
        collection_names = {
            'fine': 'engineering_manual_fine',
            'medium': 'engineering_manual_medium',
            'context': 'engineering_manual_context'
        }
        
        for chunk_type, collection_name in collection_names.items():
            try:
                collection = self.client.get_collection(collection_name)
                self.collections[chunk_type] = collection
                print(f"✅ Loaded {chunk_type} collection with {collection.count()} chunks")
            except:
                print(f"⚠️ {chunk_type} collection not found")
        
        # Fallback to single collection if multi-resolution not found
        if not self.collections:
            try:
                collection = self.client.get_collection("engineering_manual")
                self.collections['medium'] = collection
                print(f"✅ Loaded single collection with {collection.count()} chunks")
            except:
                raise Exception("No vector collections found")
        
        # Set up Claude client
        try:
            import anthropic
            api_key = st.secrets.get("CLAUDE_API_KEY")
            if not api_key:
                raise Exception("Claude API key not found in secrets")
            self.claude_client = anthropic.Anthropic(api_key=api_key)
        except Exception as e:
            raise Exception(f"Claude API setup failed: {e}")
        
        self.is_initialized = True
        print("✅ RAG Engine initialized successfully")
    
    def is_ready(self):
        """Check if the RAG engine is ready"""
        return self.is_initialized and self.client and self.claude_client
    
    def query(self, question, max_chunks=5, similarity_threshold=0.6):
        """Answer a question using the engineering manual"""
        if not self.is_ready():
            return {
                'answer': 'System not ready. Please check configuration.',
                'sources': [],
                'chunks_used': 0
            }
        
        try:
            # Search for relevant information
            relevant_chunks = self._search_manual(question, max_chunks, similarity_threshold)
            
            if not relevant_chunks:
                return {
                    'answer': 'I could not find relevant information in the Engineering Manual to answer this question. Please try rephrasing your question or ask about a different topic.',
                    'sources': [],
                    'chunks_used': 0
                }
            
            # Generate answer
            answer = self._generate_answer(question, relevant_chunks)
            
            # Prepare sources
            sources = []
            for i, chunk in enumerate(relevant_chunks, 1):
                sources.append({
                    'source_num': i,
                    'source_file': chunk.get('source', 'Engineering_Manual.docx'),
                    'chunk_id': chunk.get('chunk_id', f'chunk_{i}'),
                    'similarity': chunk.get('similarity', 0),
                    'chunk_type': chunk.get('chunk_type', 'medium')
                })
            
            return {
                'answer': answer,
                'sources': sources,
                'chunks_used': len(relevant_chunks),
                'model_used': 'claude-sonnet-4-5-20250929',
                'token_usage': {'input_tokens': 0, 'output_tokens': 0}
            }
            
        except Exception as e:
            return {
                'answer': f'Error processing question: {str(e)}',
                'sources': [],
                'chunks_used': 0
            }
    
    def _search_manual(self, question, max_chunks, similarity_threshold):
        """Search through the manual for relevant information"""
        all_chunks = []
        
        for chunk_type, collection in self.collections.items():
            try:
                results = collection.query(
                    query_texts=[question],
                    n_results=max_chunks
                )
                
                if results['documents'][0]:
                    for i in range(len(results['documents'][0])):
                        text = results['documents'][0][i]
                        metadata = results['metadatas'][0][i] if results.get('metadatas') else {}
                        
                        distance = results['distances'][0][i] if results.get('distances') else 0
                        similarity = max(0, 1 - (distance / 2))
                        
                        if similarity >= similarity_threshold:
                            all_chunks.append({
                                'text': text,
                                'similarity': similarity,
                                'chunk_type': chunk_type,
                                'chunk_id': metadata.get('chunk_id', f'{chunk_type}_{i}'),
                                'source': metadata.get('source', 'Engineering_Manual.docx')
                            })
            
            except Exception as e:
                print(f"Error searching {chunk_type} collection: {e}")
                continue
        
        # Sort by similarity and return best ones
        all_chunks.sort(key=lambda x: x['similarity'], reverse=True)
        return all_chunks[:max_chunks]
    
    def _generate_answer(self, question, chunks):
        """Generate answer using Claude AI"""
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            context_parts.append(f"[SOURCE {i}]\n{chunk['text']}")
        
        full_context = "\n\n".join(context_parts)
        
        prompt = f"""You are an expert assistant for a municipal engineering department. Answer questions using ONLY the provided context.

CONTEXT FROM ENGINEERING MANUAL:
{full_context}

QUESTION: {question}

You MUST respond using EXACTLY this format with these EXACT headers (copy them exactly):

ANSWER: [State the direct answer in one sentence with specific numbers/requirements]

DETAILS:
- [First supporting detail or related requirement]
- [Second supporting detail if applicable]
- [Additional details as needed]

CODE REFERENCE: [Section number if mentioned in sources, or "See sources below"]

SOURCES: [SOURCE X, SOURCE Y]

RULES:
- Start with "ANSWER:" immediately - no other text before it
- Keep the ANSWER line to 1-2 sentences maximum
- Use simple bullet points with "-" for DETAILS
- Do not use markdown formatting like ** or ## or ###
- Do not add any headers other than ANSWER:, DETAILS:, CODE REFERENCE:, and SOURCES:
- If information is not in the context, say "ANSWER: The Engineering Manual does not contain this information."

Respond now:"""

        try:
            response = self.claude_client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1000,
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}]
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"Error generating answer: {str(e)}"
```

---

## 🔑 Key Changes Made

| Change | Why |
|--------|-----|
| Removed `**` markdown formatting from prompt | Stops the huge bold headers |
| Changed to simple text headers (`ANSWER:`, `DETAILS:`) | Consistent, predictable format |
| Set `temperature=0.0` | More deterministic responses |
| Added explicit "no markdown" rule | Prevents `##`, `**`, `###` formatting |
| Provided exact header names to copy | Forces consistent structure |
| Simplified bullet format to `-` | Cleaner, uniform appearance |

---

## 🎯 Expected New Output
```
ANSWER: 25% of the total lot area is the maximum building coverage permitted on residential lots.

DETAILS:
- Building coverage includes primary dwelling, accessory buildings, porches/decks with roofs, garages, and carports
- Example: 20,000 sq ft lot × 0.25 = 5,000 sq ft maximum coverage
- Calculations must be shown on site plans

CODE REFERENCE: See sources below

SOURCES: [SOURCE 1, SOURCE 3, SOURCE 5]
