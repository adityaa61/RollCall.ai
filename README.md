# RollCall.ai

**Smart, automated classroom attendance powered by AI face and voice recognition.**

RollCall.ai replaces manual roll-call with a fast, AI-assisted attendance system for teachers and students — built with Streamlit and Supabase.

🔗 **Live Demo:** [add your deployed Streamlit Cloud link here]
🎥 **Demo Screenshot:**

![RollCall.ai Home Screen](add-screenshot-path-or-url-here)

---

## ✨ Features

- **Dual portals** — separate, tailored experiences for Students and Teachers
- **AI-powered attendance** — face recognition and voice-based attendance pipelines to mark attendance automatically instead of manual roll-call
- **Subject / class management** — teachers can create subjects, generate join codes, and manage sections
- **QR code class enrollment** — students scan a QR code or click a link to instantly join a class
- **Attendance review & confirmation** — teachers review AI-detected attendance before saving, avoiding false positives
- **Real-time backend** — powered by Supabase (PostgreSQL) for auth, data storage, and row-level security
- **Responsive, modern UI** — custom dark-themed interface built entirely with Streamlit + custom CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit, custom CSS |
| Backend / Database | Supabase (PostgreSQL) |
| AI / Recognition | [add: e.g. face_recognition / OpenCV / speech_recognition — fill in what your pipelines actually use] |
| QR Codes | Segno |
| Language | Python |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A [Supabase](https://supabase.com) project (free tier works)

### Installation

```bash
# Clone the repository
git clone https://github.com/[your-username]/rollcall-ai.git
cd rollcall-ai

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.streamlit/secrets.toml` file in the project root with your Supabase credentials:

```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-anon-key"
```

> ⚠️ Never commit this file. It's already excluded via `.gitignore`.

### Run locally

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📂 Project Structure

```
rollcall-ai/
├── app.py                     # Entry point, routing & page config
├── requirements.txt
├── src/
│   ├── components/            # Reusable UI components (header, footer, dialogs, cards)
│   ├── database/               # Supabase client & DB queries
│   ├── pipelines/              # Face & voice recognition pipelines
│   ├── screens/                 # Home, student, teacher screens
│   └── ui/                       # Shared layout & styling
└── assets/                    # Logo and static assets
```

---

## 🗺️ Roadmap / Future Improvements

- [ ] Email notifications for attendance summaries
- [ ] Exportable attendance reports (CSV/PDF)
- [ ] Analytics dashboard for attendance trends
- [ ] Mobile-optimized layout

---

## 👤 Author

Built by **[Aditya Singh]** — [https://www.linkedin.com/in/aditya-singh-as-dev/] · [your portfolio/GitHub]


---

