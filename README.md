# Resume Builder

A Python/Flask web app for making quick, tailored edits to your resume **without ever touching the layout**.

## Why this exists

Every job application deserves a resume tailored to that job. But copying and pasting between documents in Word means spending time re-fixing fonts, spacing, and alignment every single time. Resume Builder separates *content* from *layout*: you edit the content (title, bullets, skills, etc.), and the layout stays exactly the same.

## Status

🚧 **Early development.** The project is a work in progress and is not yet usable end to end.

**Currently in place**
- Flask app skeleton with a landing page ("Build Resume" / "Load & Edit Resume")
- Name and desired-title input pages
- Data models for work experience, bullets, contact info, projects, certifications, and categorized skills

**Not yet built**
- Work experience input page and route
- Loading and editing a saved resume
- Remaining sections (contact info, projects, certifications, education, skills)
- Saving and exporting

## Planned features

### Resume sections
- Name and desired title
- Contact info (email, city/state, LinkedIn) with format checking
- Work experience: job title, company, location, start/end dates, and up to five bullets per job
- Projects: title and description
- Certifications: title/issuer and date obtained
- Education: school, degree, completion status, and optional relevant coursework
  - Unfinished degrees show an estimated completion date so they never read as completed
- Skills: optional categories, add/remove/edit single or multiple skills, easy-to-manipulate skill pool

### Behavior
- Input is normalized for comparison (lowercased) and formatted for display (e.g., capitalized skills, leaving small words like *with*, *as*, *in*, *of*, *or*, *on* lowercase)
- Each section can be added, edited, and output
- Optional items (such as categories and relevant coursework) can be toggled on or off per resume

### Output formats
- `.pdf`
- `.doc`
- `.html`
- `.json` (for saving and reloading)

## Tech stack

- Python 3
- [Flask](https://flask.palletsprojects.com/)
- HTML (Jinja templates)

## Getting started

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install flask

# Run the app
python app.py
```

Then open <http://127.0.0.1:5000> in your browser.

## Project structure

```
.
├── app.py                          # Flask routes
├── models.py                       # Resume data models and app-level constants
├── Planner.md                      # Design plan and feature checklist
├── testspace.py                    # Scratch file for testing ideas
└── templates/
    ├── index.html                  # Landing page
    ├── buildresume_Name.html       # Name input
    ├── buildresume_Title.html      # Desired title input
    ├── buildresume_Work_Experience.html
    └── loadresume.html             # Load & edit a saved resume
```

> Flask expects templates in a `templates/` folder. If yours are currently next to `app.py`, move them there.

## Roadmap

- [x] Landing page
- [x] Name and title input
- [ ] Work experience input
- [ ] Contact info, projects, certifications, education, skills
- [ ] Save/load resumes (JSON)
- [ ] Fixed-layout export to PDF, DOC, and HTML

## Contributing

This is a personal project, but suggestions and issues are welcome.

## License

Not yet specified. Consider adding a license such as [MIT](https://choosealicense.com/licenses/mit/) before publishing.
