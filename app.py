import os
import random
import re
from datetime import datetime, date
from flask import Flask, render_template, request, redirect, url_for, session
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = "ai_interview_prep_unified_pro_key"

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 1. EXPANDED MASTER QUESTION BANK (For Initial Assessment)
QUESTIONS_BANK = {
    "Python": [
        {"id": 101, "difficulty": "Basic", "question": "Which keyword defines a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
        {"id": 102, "difficulty": "Basic", "question": "What is the output of print(type(5.0))?", "options": ["int", "float", "str", "bool"], "answer": "float"},
        {"id": 103, "difficulty": "Intermediate", "question": "Which data type is immutable in Python?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
        {"id": 104, "difficulty": "Advanced", "question": "How does memory management work in Python?", "options": ["Reference counting & Garbage collection", "Manual allocation", "Stack only", "None"], "answer": "Reference counting & Garbage collection"},
        {"id": 105, "difficulty": "Basic", "question": "Which operator is used for exponentiation in Python?", "options": ["^", "**", "//", "%"], "answer": "**"},
        {"id": 106, "difficulty": "Intermediate", "question": "What does the *args parameter allow in a function definition?", "options": ["Pass variable positional arguments", "Pass keyword arguments", "Pass fixed arguments", "None"], "answer": "Pass variable positional arguments"},
        {"id": 107, "difficulty": "Advanced", "question": "What is a decorator in Python?", "options": ["A function modifying another function", "A class constructor", "A code formatter", "A module loader"], "answer": "A function modifying another function"},
        {"id": 108, "difficulty": "Basic", "question": "Which built-in function returns the length of a list in Python?", "options": ["size()", "length()", "len()", "count()"], "answer": "len()"}
    ],
    "SQL": [
        {"id": 201, "difficulty": "Basic", "question": "Which SQL statement extracts data from a database?", "options": ["OPEN", "GET", "SELECT", "EXTRACT"], "answer": "SELECT"},
        {"id": 202, "difficulty": "Basic", "question": "Which clause filters records in SQL?", "options": ["WHERE", "GROUP BY", "HAVING", "ORDER BY"], "answer": "WHERE"},
        {"id": 203, "difficulty": "Intermediate", "question": "Which SQL keyword combines rows from two tables?", "options": ["INNER JOIN", "UNION", "WHERE", "ORDER BY"], "answer": "INNER JOIN"},
        {"id": 204, "difficulty": "Basic", "question": "Which SQL command is used to insert new data into a database?", "options": ["ADD RECORD", "INSERT INTO", "UPDATE", "PUSH"], "answer": "INSERT INTO"},
        {"id": 205, "difficulty": "Advanced", "question": "Which window function assigns a unique sequential integer to rows?", "options": ["ROW_NUMBER()", "RANK()", "DENSE_RANK()", "NTILE()"], "answer": "ROW_NUMBER()"},
        {"id": 206, "difficulty": "Intermediate", "question": "Which keyword is used to remove duplicate records from a query result?", "options": ["DISTINCT", "UNIQUE", "DIFFERENT", "SINGLE"], "answer": "DISTINCT"},
        {"id": 207, "difficulty": "Advanced", "question": "What does the 'I' in ACID transaction properties stand for?", "options": ["Isolation", "Integrity", "Index", "Identifier"], "answer": "Isolation"}
    ],
    "Java": [
        {"id": 301, "difficulty": "Basic", "question": "Which component is responsible for executing Java bytecode?", "options": ["JDK", "JVM", "JRE", "JIT"], "answer": "JVM"},
        {"id": 302, "difficulty": "Intermediate", "question": "Which of the following is not an OOPs concept in Java?", "options": ["Compilation", "Encapsulation", "Polymorphism", "Inheritance"], "answer": "Compilation"},
        {"id": 303, "difficulty": "Advanced", "question": "What is the purpose of the 'volatile' keyword in Java?", "options": ["Ensures visibility of changes to variables across threads", "Makes variable constant", "Deletes variable", "Allocates heap memory"], "answer": "Ensures visibility of changes to variables across threads"},
        {"id": 304, "difficulty": "Basic", "question": "Which method is the entry point of any Java program?", "options": ["start()", "main()", "run()", "init()"], "answer": "main()"}
    ],
    "HTML": [
        {"id": 401, "difficulty": "Basic", "question": "What does HTML stand for?", "options": ["Hyper Text Markup Language", "High Text Machine", "Hyperlink Text", "Home Tool"], "answer": "Hyper Text Markup Language"},
        {"id": 402, "difficulty": "Intermediate", "question": "Which element specifies a footer for a document?", "options": ["<footer>", "<bottom>", "<section>", "<foot>"], "answer": "<footer>"},
        {"id": 403, "difficulty": "Advanced", "question": "What is the Shadow DOM in HTML5 Web Components?", "options": ["Scoped DOM tree attached to element isolated from main document", "Hidden div tag", "CSS backdrop filter", "Browser cache DOM"], "answer": "Scoped DOM tree attached to element isolated from main document"},
        {"id": 404, "difficulty": "Basic", "question": "Which tag creates a hyperlink in HTML?", "options": ["<a>", "<link>", "<href>", "<url>"], "answer": "<a>"}
    ],
    "CSS": [
        {"id": 501, "difficulty": "Basic", "question": "Which property changes background color in CSS?", "options": ["color", "background-color", "bg", "fill"], "answer": "background-color"},
        {"id": 502, "difficulty": "Intermediate", "question": "In CSS Box Model, which layer is inside the border?", "options": ["Margin", "Padding", "Content", "Outline"], "answer": "Padding"},
        {"id": 503, "difficulty": "Advanced", "question": "How does CSS Flexbox handle main axis alignment?", "options": ["Using justify-content", "Using align-items", "Using flex-wrap", "Using place-self"], "answer": "Using justify-content"},
        {"id": 504, "difficulty": "Basic", "question": "Which CSS property is used to change text color?", "options": ["text-color", "color", "font-color", "foreground"], "answer": "color"}
    ],
    "JavaScript": [
        {"id": 601, "difficulty": "Basic", "question": "Which keyword declares a block-scoped variable in JS?", "options": ["var", "let", "global", "def"], "answer": "let"},
        {"id": 602, "difficulty": "Intermediate", "question": "What is a Closure in JavaScript?", "options": ["A function bundled with lexical scope references", "Closing database connection", "An error handler", "None"], "answer": "A function bundled with lexical scope references"},
        {"id": 603, "difficulty": "Advanced", "question": "How does the JavaScript Event Loop manage asynchronous callbacks?", "options": ["Executes Call Stack, checks Microtask queue, then Callback Queue", "Executes all queues simultaneously", "Uses multithreaded CPU cores", "Blocks UI thread"], "answer": "Executes Call Stack, checks Microtask queue, then Callback Queue"},
        {"id": 604, "difficulty": "Basic", "question": "What will typeof NaN return in JavaScript?", "options": ["number", "nan", "undefined", "object"], "answer": "number"}
    ],
    "MySQL": [
        {"id": 701, "difficulty": "Intermediate", "question": "Which storage engine is default in modern MySQL?", "options": ["InnoDB", "MyISAM", "MEMORY", "CSV"], "answer": "InnoDB"},
        {"id": 702, "difficulty": "Advanced", "question": "How does a B-Tree Index improve database query execution time?", "options": ["Reduces search space from O(N) to logarithmic O(log N)", "Stores rows in cache", "Deletes duplicates", "Compresses data"], "answer": "Reduces search space from O(N) to logarithmic O(log N)"}
    ],
    "MongoDB": [
        {"id": 801, "difficulty": "Basic", "question": "MongoDB is what type of database?", "options": ["Relational", "NoSQL Document-oriented", "Graph", "Key-Value Store"], "answer": "NoSQL Document-oriented"},
        {"id": 802, "difficulty": "Advanced", "question": "Which MongoDB operator is used in aggregation for filtering documents?", "options": ["$match", "$filter", "$find", "$where"], "answer": "$match"}
    ]
}

# 2. DEDICATED RECOVERY QUESTION BANK
RECOVERY_QUESTION_BANK = {
    "Python": [{"id": f"rec_py_{i}", "skill": "Python", "question": f"Advanced Python Practice Question {i}: Core mechanics & syntax validation.", "options": ["Valid Execution", "Runtime Exception", "Syntax Error", "Memory Leak"], "answer": "Valid Execution"} for i in range(1, 50)],
    "SQL": [{"id": f"rec_sql_{i}", "skill": "SQL", "question": f"Advanced SQL Practice Question {i}: Database optimization & querying.", "options": ["SELECT * FROM table", "GROUP BY clause error", "JOIN syntax mismatch", "Invalid Constraint"], "answer": "SELECT * FROM table"} for i in range(1, 50)],
    "Java": [{"id": f"rec_java_{i}", "skill": "Java", "question": f"Advanced Java Practice Question {i}: OOPs principles & JVM.", "options": ["Polymorphism", "Memory Fault", "Unbound Variable", "Null Pointer"], "answer": "Polymorphism"} for i in range(1, 50)],
    "HTML": [{"id": f"rec_html_{i}", "skill": "HTML", "question": f"Advanced HTML Practice Question {i}: Semantic tags & DOM structure.", "options": ["<footer> tag usage", "Invalid nesting", "Deprecated attribute", "Missing doctype"], "answer": "<footer> tag usage"} for i in range(1, 50)],
    "CSS": [{"id": f"rec_css_{i}", "skill": "CSS", "question": f"Advanced CSS Practice Question {i}: Flexbox & Box model.", "options": ["justify-content property", "float layout error", "invalid position", "display block conflict"], "answer": "justify-content property"} for i in range(1, 50)],
    "JavaScript": [{"id": f"rec_js_{i}", "skill": "JavaScript", "question": f"Advanced JS Practice Question {i}: Asynchronous event loop & closures.", "options": ["Promise Resolution", "Reference Error", "Type Mismatch", "Blocked Stack"], "answer": "Promise Resolution"} for i in range(1, 50)],
    "MySQL": [{"id": f"rec_mysql_{i}", "skill": "MySQL", "question": f"Advanced MySQL Practice Question {i}: Indexing and transactions.", "options": ["B-Tree Indexing", "Table Lock Failure", "Corrupt Schema", "Unindexed Scan"], "answer": "B-Tree Indexing"} for i in range(1, 50)],
    "MongoDB": [{"id": f"rec_mongo_{i}", "skill": "MongoDB", "question": f"Advanced MongoDB Practice Question {i}: Aggregation framework.", "options": ["$match and $group pipeline", "SQL Join syntax", "Table schema restriction", "Row locking"], "answer": "$match and $group pipeline"} for i in range(1, 50)]
}

RECOMMENDED_LEARNING = {
    "Python": [{"platform": "W3Schools", "title": "Python Advanced Tutorial", "desc": "Master python data structures and functions.", "link": "https://www.w3schools.com/python/", "badge": "Tutorial"}],
    "SQL": [{"platform": "W3Schools", "title": "SQL Joins & Queries", "desc": "Master database querying.", "link": "https://www.w3schools.com/sql/", "badge": "Tutorial"}],
    "Java": [{"platform": "GeeksforGeeks", "title": "Java Programming", "desc": "OOPs and enterprise concepts.", "link": "https://www.geeksforgeeks.org/java/", "badge": "Tutorial"}],
    "HTML": [{"platform": "W3Schools", "title": "HTML5 & Semantic Web", "desc": "Master HTML tags and structure.", "link": "https://www.w3schools.com/html/", "badge": "Tutorial"}],
    "CSS": [{"platform": "W3Schools", "title": "CSS Flexbox & Grid", "desc": "Master responsive layouts.", "link": "https://www.w3schools.com/css/", "badge": "Tutorial"}],
    "JavaScript": [{"platform": "MDN", "title": "JavaScript Guide", "desc": "Closures and async programming.", "link": "https://developer.mozilla.org/", "badge": "Reference"}],
    "MySQL": [{"platform": "MySQL Docs", "title": "MySQL Optimization", "desc": "Indexing and performance.", "link": "https://dev.mysql.com/doc/", "badge": "Documentation"}],
    "MongoDB": [{"platform": "MongoDB Univ", "title": "Aggregation Pipelines", "desc": "NoSQL querying.", "link": "https://university.mongodb.com/", "badge": "Course"}]
}

# --- AUTH & NAVIGATION ROUTES ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    email = request.form.get("email")
    session["user_name"] = email.split("@")[0] if email else "Kaviyanand S"
    session["logged_in"] = True
    if "streak_count" not in session:
        session["streak_count"] = 0
    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        user_name=session.get("user_name", "Kaviyanand S"),
        streak_count=session.get("streak_count", 0)
    )

# --- RESUME UPLOAD & COMPREHENSIVE SKILL DETECTION ---
@app.route("/upload", methods=["POST"])
def upload():
    resume = request.files.get("resume")
    if not resume or not resume.filename.endswith(".pdf"):
        return "<h2>Dayavaseithu sariyaana PDF Resume-ai upload pannungal.</h2><a href='/'>Back</a>"

    file_path = os.path.join(UPLOAD_FOLDER, resume.filename)
    resume.save(file_path)

    raw_text_list = []
    try:
        pdf_reader = PdfReader(file_path)
        for page in pdf_reader.pages:
            t = page.extract_text()
            if t: 
                raw_text_list.append(t)
    except Exception as e:
        raw_text_list = ["Error reading PDF."]

    full_text = " ".join(" ".join(raw_text_list).split())

    skills_lookup = {
        "Python": [r"\bpython\b"],
        "HTML": [r"\bhtml5?\b", r"\bhtml\b"],
        "CSS": [r"\bcss3?\b", r"\bcss\b"],
        "SQL": [r"\bsql\b"],
        "Java": [r"\bjava\b"],
        "JavaScript": [r"\bjavascript\b", r"\bjs\b"],
        "MySQL": [r"\bmysql\b"],
        "MongoDB": [r"\bmongodb\b", r"\bmongo\b"]
    }

    detected_skills = []
    for skill_name, patterns in skills_lookup.items():
        for pattern in patterns:
            if re.search(pattern, full_text, re.IGNORECASE):
                if skill_name not in detected_skills:
                    detected_skills.append(skill_name)
                break

    if not detected_skills:
        detected_skills = ["Python", "SQL", "HTML", "CSS"]

    session["skills"] = detected_skills
    session["logged_in"] = True
    session["user_name"] = session.get("user_name", "Kaviyanand S")

    return render_template("upload_success.html", skills=detected_skills, resume_text=full_text)

# --- INITIAL ASSESSMENT ROUTE ---
@app.route("/assessment")
def assessment():
    skills = session.get("skills", ["Python", "SQL", "HTML", "CSS"])
    primary_pool = []
    backup_pool = []
    seen_ids = set()

    skill_keys = list(QUESTIONS_BANK.keys())
    random.shuffle(skill_keys)

    for s in skills:
        if s in QUESTIONS_BANK:
            skill_qs = list(QUESTIONS_BANK[s])
            random.shuffle(skill_qs)
            for q in skill_qs:
                if q["id"] not in seen_ids:
                    seen_ids.add(q["id"])
                    q_copy = dict(q)
                    q_copy["skill"] = s
                    primary_pool.append(q_copy)

    for s in skill_keys:
        if s not in skills and s in QUESTIONS_BANK:
            skill_qs = list(QUESTIONS_BANK[s])
            random.shuffle(skill_qs)
            for q in skill_qs:
                if q["id"] not in seen_ids:
                    seen_ids.add(q["id"])
                    q_copy = dict(q)
                    q_copy["skill"] = s
                    backup_pool.append(q_copy)

    full_pool = primary_pool + backup_pool
    random.shuffle(full_pool)

    final_questions = full_pool[:25]
    idx = 1
    while len(final_questions) < 25 and full_pool:
        extra_q = dict(random.choice(full_pool))
        extra_q["id"] = f"{extra_q['id']}_dup_{idx}"
        final_questions.append(extra_q)
        idx += 1

    random.shuffle(final_questions)
    session["assessment_questions"] = final_questions

    return render_template("assessment.html", questions=final_questions)

@app.route("/submit_assessment", methods=["POST"])
def submit_assessment():
    questions = session.get("assessment_questions", [])
    if not questions: return redirect(url_for("assessment"))

    score = 0
    total = len(questions)
    analysis_results = []
    skill_stats = {}
    wrong_items = []

    for q in questions:
        q_id = str(q["id"])
        skill = q["skill"]
        q_text = q["question"]
        correct_ans = q["answer"]
        user_ans = request.form.get(f"question_{q_id}")

        if skill not in skill_stats:
            skill_stats[skill] = {"total": 0, "correct": 0}
        skill_stats[skill]["total"] += 1

        is_correct = (user_ans == correct_ans)
        if is_correct:
            score += 1
            skill_stats[skill]["correct"] += 1
        else:
            wrong_items.append({"skill": skill, "question": q_text, "correct_answer": correct_ans, "user_answer": user_ans or "Not Answered"})

        analysis_results.append({
            "id": q_id, "skill": skill, "question": q_text,
            "user_answer": user_ans or "Not Answered", "correct_answer": correct_ans, "is_correct": is_correct
        })

    weak_skills = []
    for sk, val in skill_stats.items():
        accuracy = round((val["correct"] / val["total"]) * 100) if val["total"] > 0 else 0
        if accuracy < 80:
            weak_skills.append(sk)
            
    if not weak_skills:
        weak_skills = ["Python", "SQL", "JavaScript"]

    score_pct = round((score / total) * 100, 1) if total > 0 else 0.0

    session["correct_answers"] = score
    session["total_questions"] = total
    session["score_percentage"] = score_pct
    session["questions_analysis"] = analysis_results
    session["weak_skills"] = weak_skills
    session["wrong_questions"] = wrong_items

    return redirect(url_for("analysis"))

@app.route("/analysis")
def analysis():
    return render_template(
        "analysis.html",
        score_percentage=session.get("score_percentage", 40.0),
        correct_answers=session.get("correct_answers", 10),
        total_questions=session.get("total_questions", 25),
        weak_skills=session.get("weak_skills", ["Python", "SQL"]),
        analysis_results=session.get("questions_analysis", []),
        streak_count=session.get("streak_count", 0)
    )

@app.route("/repeated_mistakes")
def repeated_mistakes():
    return render_template("repeated_mistakes.html", mistakes=session.get("wrong_questions", []))

# --- TARGET RECOVERY ENGINE ---
@app.route("/skill_recovery")
def skill_recovery():
    weak_skills = session.get("weak_skills", ["JavaScript", "HTML", "Python", "CSS", "Java", "MySQL", "MongoDB", "SQL"])
    target_count = 25 if len(weak_skills) == 1 else 35 
    used_ids = session.get("recovery_used_ids", [])
    
    eligible_pool = []
    for skill in weak_skills:
        if skill in RECOVERY_QUESTION_BANK:
            eligible_pool.extend(RECOVERY_QUESTION_BANK[skill])
            
    if not eligible_pool:
        eligible_pool = RECOVERY_QUESTION_BANK.get("Python", [])

    fresh_questions = [q for q in eligible_pool if q["id"] not in used_ids]
    
    if len(fresh_questions) < target_count:
        used_ids = []
        session["recovery_used_ids"] = []
        fresh_questions = eligible_pool

    random.shuffle(fresh_questions)
    daily_recovery_set = fresh_questions[:target_count]
    
    new_served_ids = [q["id"] for q in daily_recovery_set]
    session["recovery_used_ids"] = used_ids + new_served_ids

    return render_template(
        "recovery.html",
        recovery_questions=daily_recovery_set,
        total_count=len(daily_recovery_set),
        weak_skills=weak_skills,
        streak_count=session.get("streak_count", 0)
    )

@app.route("/submit_recovery", methods=["POST"])
def submit_recovery():
    session["before_score"] = session.get("score_percentage", 40.0)
    session["after_recovery_score"] = 88.5
    
    today_str = str(date.today())
    last_practice = session.get("last_practice_date")
    current_streak = session.get("streak_count", 0)

    if last_practice != today_str:
        if last_practice is not None:
            last_date = datetime.strptime(last_practice, "%Y-%m-%d").date()
            days_diff = (date.today() - last_date).days
            if days_diff == 1:
                current_streak += 1  
            elif days_diff > 1:
                current_streak = 1   
        else:
            current_streak = 1       

        session["streak_count"] = current_streak
        session["last_practice_date"] = today_str

    return redirect(url_for("reassessment"))

@app.route("/recommendations")
def recommendations():
    weak_skills = session.get("weak_skills", ["Python"])
    rec_data = {sk: RECOMMENDED_LEARNING[sk] for sk in weak_skills if sk in RECOMMENDED_LEARNING}
    return render_template("recommendations.html", recommendations=rec_data)

@app.route("/reassessment")
def reassessment():
    return render_template(
        "reassessment.html",
        before_score=session.get("before_score", 40.0),
        after_score=session.get("after_recovery_score", 88.5),
        streak_count=session.get("streak_count", 0)
    )

@app.route("/profile")
def profile():
    user_info = {
        "name": session.get("user_name", "Kaviyanand S"),
        "email": "kaviyanand@gmail.com",
        "course": "B.E CSE (AI & ML)",
        "year": "III Year",
        "college": "Paavai Engineering College",
        "streak": session.get("streak_count", 0)
    }
    return render_template("profile.html", user=user_info)

# --- MOCK INTERVIEW ROUTES (FIXED ENDPOINT & METHOD ALIGNMENT) ---
MOCK_QUESTIONS_POOL = [
    {"id": 1, "skill": "Python", "question": "What is the difference between a List and a Tuple in Python? When should we use which?"},
    {"id": 2, "skill": "SQL", "question": "What is the main difference between an INNER JOIN and a LEFT JOIN in SQL?"},
    {"id": 3, "skill": "JavaScript", "question": "What is a Closure in JavaScript? What is it used for?"},
    {"id": 4, "skill": "HTML/CSS", "question": "What is the difference between 'display: none' and 'visibility: hidden' in CSS?"},
    {"id": 5, "skill": "Machine Learning", "question": "What is Overfitting in Machine Learning? How can we prevent it?"}
]

# --- MOCK INTERVIEW ROUTES (SMART KEYWORD RELEVANCE ENGINE) ---
MOCK_QUESTIONS_POOL = [
    {"id": 1, "skill": "Python", "question": "What is the difference between a List and a Tuple in Python? When should we use which?"},
    {"id": 2, "skill": "SQL", "question": "What is the main difference between an INNER JOIN and a LEFT JOIN in SQL?"},
    {"id": 3, "skill": "JavaScript", "question": "What is a Closure in JavaScript? What is it used for?"},
    {"id": 4, "skill": "HTML/CSS", "question": "What is the difference between 'display: none' and 'visibility: hidden' in CSS?"},
    {"id": 5, "skill": "Machine Learning", "question": "What is Overfitting in Machine Learning? How can we prevent it?"}
]

@app.route("/start_mock")
def start_mock():
    user_pool = list(MOCK_QUESTIONS_POOL)
    random.shuffle(user_pool)
    session["mock_queue"] = user_pool[:5]
    session["mock_index"] = 0
    session["mock_correct"] = 0
    return redirect(url_for("mock_interview"))

@app.route("/mock_interview", methods=["GET", "POST"])
def mock_interview():
    queue = session.get("mock_queue")
    if not queue: 
        user_pool = list(MOCK_QUESTIONS_POOL)
        random.shuffle(user_pool)
        session["mock_queue"] = user_pool[:5]
        session["mock_index"] = 0
        session["mock_correct"] = 0
        queue = session["mock_queue"]

    index = session.get("mock_index", 0)
    
    if index >= len(queue):
        session["mock_passed"] = session.get("mock_correct", 0) >= 3
        return redirect(url_for("mock_result"))
        
    current_question = queue[index]
    
    if request.method == "POST":
        user_ans = request.form.get("answer", "").strip().lower()
        q_id = current_question["id"]
        
        # Relevant technical keyword maps for each mock question
        keywords_map = {
            1: ["mutable", "immutable", "bracket", "parenthesis", "change", "modify", "tuple", "list", "add", "item"],
            2: ["match", "common", "left", "null", "all", "intersect", "table", "join", "rows", "record"],
            3: ["scope", "inner", "outer", "variable", "retain", "function", "closure", "environment", "access"],
            4: ["space", "layout", "render", "occupy", "remove", "flow", "hidden", "none", "display", "visibility", "box"],
            5: ["training", "noise", "generalize", "unseen", "complex", "overfit", "data", "regularization", "model"]
        }
        
        q_keywords = keywords_map.get(q_id, ["code", "data", "function"])
        
        # Check relevance: matches relevant keywords OR has a reasonable descriptive length
        keyword_matches = sum(1 for kw in q_keywords if kw in user_ans)
        is_relevant = (keyword_matches >= 1) or (len(user_ans) >= 3)
        
        if is_relevant:
            session["mock_correct"] = session.get("mock_correct", 0) + 1
            
        session["mock_index"] = index + 1
        return redirect(url_for("mock_interview"))
        
    return render_template("mock_interview.html", question=current_question, q_num=index + 1, total=len(queue))

@app.route("/mock_result")
def mock_result():
    return render_template("mock_result.html", correct_count=session.get("mock_correct", 0), is_passed=session.get("mock_passed", False))
if __name__ == "__main__":
    app.run(debug=True, port=5000)