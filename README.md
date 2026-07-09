# RollCall.ai

**Smart, automated classroom attendance powered by AI face and voice recognition.**

RollCall.ai replaces manual roll-call with a fast, AI-assisted attendance system for teachers and students — built with Streamlit and Supabase.

🔗 **Live Demo:** [(https://rollcallai-mzmnd846xw89ux9osq2ixp.streamlit.app/)]


![RollCall.ai Home Screen](https://rollcallai-mzmnd846xw89ux9osq2ixp.streamlit.app/)

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

Built by **[Aditya Singh]** — [https://www.linkedin.com/in/aditya-singh-as-dev/]


---

