# recovery_question_bank.py
# Dedicated Question Bank specifically for Target Weak Skill Recovery (25/35 Rule Engine)

RECOVERY_QUESTION_BANK = {
    "Python": [
        {
            "id": f"rec_py_{i}",
            "skill": "Python",
            "subtopic": "Advanced Python Recovery Module",
            "question": f"[Recovery Python Q{i}] Deep-dive technical question on Python core mechanics and execution flow variant {i}:",
            "options": ["Accurate Technical Concept", "Syntax Exception Error", "Runtime Memory Leak", "Deprecated Implementation"],
            "answer": "Accurate Technical Concept"
        }
        for i in range(1, 40) # 40 dedicated recovery questions for Python
    ],
    "SQL": [
        {
            "id": f"rec_sql_{i}",
            "skill": "SQL",
            "subtopic": "Advanced SQL Recovery Module",
            "question": f"[Recovery SQL Q{i}] Complex database optimization or join requirement query variant {i}:",
            "options": ["SELECT optimized_query FROM db", "GROUP BY syntax violation", "CORRUPT INDEX reference", "INVALID FOREIGN KEY"],
            "answer": "SELECT optimized_query FROM db"
        }
        for i in range(1, 40) # 40 dedicated recovery questions for SQL
    ],
    "JavaScript": [
        {
            "id": f"rec_js_{i}",
            "skill": "JavaScript",
            "subtopic": "Advanced JavaScript Recovery Module",
            "question": f"[Recovery JS Q{i}] Asynchronous execution, closure, or DOM event loop variant {i}:",
            "options": ["Resolved Promise / Async Handler", "Uncaught Type Exception", "Undefined Variable Scope", "Blocked Event Loop"],
            "answer": "Resolved Promise / Async Handler"
        }
        for i in range(1, 40)
    ]
}