# MikBot

MikBot is a responsive PWA chatbot that teaches using Bloom's Taxonomy with a "plain words, experience-first" mentor persona.

## Features

-   **Persona**: Supportive, realistic, experience-based teaching.
-   **Tech Stack**: Flask, Google Gemini API, Tailwind CSS, Bootstrap Icons.
-   **PWA**: Installable on mobile and desktop.
-   **Design**: Premium dark mode aesthetic.

## Setup

1.  **Clone the repository** (if applicable).
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment**:
    -   Windows: `.\venv\Scripts\Activate`
    -   Mac/Linux: `source venv/bin/activate`
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up Environment Variables**:
    -   Copy `.env.template` to `.env`.
    -   Add your `GOOGLE_API_KEY`.
6.  **Run the application**:
    ```bash
    python app.py
    ```
7.  **Open in Browser**:
    -   Go to `http://localhost:5000`.

## PWA Icons
Note: The `manifest.json` references icons in `static/icons/`. Please add `icon-192x192.png` and `icon-512x512.png` to that directory to enable full PWA installability.

## Deployment (Vercel)

1.  **Install Vercel CLI**: `npm i -g vercel`
2.  **Login**: `vercel login`
3.  **Deploy**: `vercel`
4.  **Environment Variables**:
    -   Go to your Vercel project settings.
    -   Add `GOOGLE_API_KEY` with your API key.

