# 1. Project Overview

**The Problem.** State the causes as you understand them, who the stakeholders are and briefly mention what similar apps exist in the market (at least one) and why they fall short.
Group travel planning often leads to chaotic communication and manual expense tracking. Our main stakeholders are group travelers and independent explorers seeking seamless coordination. Existing apps like Wanderlog handle basic itinerary building well but fall short in collaboration: they lack built-in voting for group decisions and automated expense splitting, forcing users to juggle multiple apps like WhatsApp for debates and Splitwise for bills.

**Our Solution.** What it is in 3-4 sentences, then list out your feature-set.
TripPOP is a collaborative travel platform designed to eliminate the logistical friction of group trips. We consolidate interactive itinerary building, real-time group voting, and automated financial tracking into a single unified dashboard. By integrating AI for instant receipt scanning, smart weather adaptations, and real-time group location tracking, it transforms travel coordination from an administrative chore into a seamless shared adventure.

**Feature-Set:**
*   **Democratic Group Voting:** Built-in polls for members to propose and agree on destinations without messy group chats.
*   **AI Vision Receipt Splitter:** Uses the Gemini Multimodal API to scan physical receipts, automatically extracting items and costs for instant group expense splitting.
*   **Collaborative Itinerary & Live Map:** A shared, real-time timeline where all group members can view and edit the daily schedule together, alongside real-time friend location tracking to prevent anyone from getting lost.
*   **Smart Disruption Response:** Automatically suggests viable alternative plans (e.g., indoor activities) when sudden weather changes affect the itinerary.

## 2. Ideation & Process

**2.1 Ideas We Considered**

| Idea | Why it was dropped / kept |
| :--- | :--- |
| **AI Vision Receipt Splitter (Gemini API)** | **Kept.** Solves the biggest friction in group travel (money arguments). Highly feasible with Gemini's Multimodal API and adds strong technical value. |
| **Democratic Group Voting System** | **Kept.** Directly addresses decision paralysis in group chats. Low technical complexity but extremely high value for user experience. |
| **Live Group Location Tracking** | **Kept.** Eliminates the constant "where are you?" texts during free-and-easy itinerary blocks by showing members directly on the shared trip map. |
| **Social Travel Feed & Cloneable Itineraries** | **Dropped.** We decided to pivot away from social networking features to maintain a strict focus on utility and logistics (planning, money, location) for our MVP. |
| **In-App Group Chat** | **Dropped.** Users already use established messaging apps like WhatsApp/Telegram. Forcing them to use another chat interface creates friction; our voting and live map features solve coordination without needing a chat module. |
| **Real-time Flight & Hotel Price Aggregator** | **Dropped.** Third-party flight APIs (like Amadeus/Skyscanner) are expensive and rate-limited. It shifts focus away from our core goal (group coordination) to booking, which is already saturated. |

**2.2 Ideation Boards**
*(Insert your mindmaps, SCAMPER grids, or flowcharts here)*

**2.3 Mentor Consultation**

| Date | Mentor | Feedback Received | What Was Changed |
| :--- | :--- | :--- | :--- |
| *(Fill)* | *(Fill)* | *(Fill)* | *(Fill)* |

## 3. Design & Prototype

**UI Prototype:** 

**1. Home Dashboard & AI Assistant**
![Home Dashboard](Screenshot 2026-09-11 143645.jpg)
![AI Assistant Prompt](Screenshot 2026-09-11 142818.png)
*The main landing page allows users to view their saved collaborative trips or instantly generate a new plan using the AI assistant prompt.*

**2. Collaborative Itinerary**
![Collaborative Itinerary](Screenshot 2026-09-11 143710.jpg)
*A shared workspace where all group members can view the daily schedule, add activities, and preview location markers on an interactive map.*

**3. Live Trip Map & Tracking**
![Live Trip Map](Screenshot 2026-09-11 143723.png)
*Real-time map tracking to locate friends and see how far they are from upcoming itinerary stops, reducing the "where are you?" texts.*

**4. Democratic Voting System**
![Voting System](Screenshot 2026-09-11 143852.png)
*An active polling dashboard where members vote on activities (e.g., lunch spots or night markets). Consensus automatically updates the live itinerary.*

**5. Smart Disruption Response**
![Disruption Response](Screenshot 2026-09-11 143749.png)
*Dynamic re-routing alerts that notify the group of issues (like heavy rain) and instantly suggest indoor alternatives to keep the trip on track.*

**6. Budgeting Dashboard**
![Budgeting Dashboard](Screenshot 2026-09-11 143738.png)
*A financial overview that breaks down category spending and tracks total group expenses against the set trip budget.*

**7. Split Studio (AI Receipt Scanner)**
![Split Studio](Screenshot 2026-09-11 143838.jpg)
*Using AI vision, users can upload a receipt. The system automatically extracts line items, assigns costs to specific group members, and calculates settlements.*

## 4. What Makes It Different

Unlike traditional travel apps that force users to jump between different tools for planning, chatting, and splitting bills, TripPOP creates a seamless, utility-driven ecosystem. Here is what makes our approach novel:

*   **AI Vision Expense Splitting (The Twist):**
    Instead of manually typing every receipt item into an app like Splitwise, users simply snap a photo. By leveraging the Gemini Multimodal API, our app instantly parses line items, prices, and currencies, directly integrating the split costs into the group's travel dashboard.
*   **Actionable Democratic Voting (The Twist):**
    Most groups debate on WhatsApp and then manually update a planner. Our twist is native polling: members vote on destinations within the app, and the winning location is automatically scheduled and routed in the shared itinerary.
*   **Live Group Logistics (The Twist):**
    Instead of relying on fragmented communication to coordinate meetups, our live map integrates friend locations directly beside the itinerary stops. You always know if someone is falling behind schedule without having to text them.

**Competitor Comparison**

| Feature | TripPOP (Our App) | Wanderlog | Agoda |
| :--- | :--- | :--- | :--- |
| Collaborative Itinerary | ✅ | ✅ | ❎ |
| Native Group Voting | ✅ | ❎ | ❎ |
| AI Receipt Scanning | ✅ | ❎ | ❎ |
| Live Friend Tracking | ✅ | ❎ | ❎ |
| Integrated Bill Splitting | ✅ | ❎ | ❎ |

## 5. Technical Architecture & Feasibility

**Tech stack**
*   **Frontend: HTML, Tailwind CSS, HTMX, and Alpine.js rendered via Flask-Jinja2:**
    *   *Why:* This combination (often called the "HAFT" stack) provides a reactive, modern app feel without the massive build complexity of React. HTMX handles server requests directly from HTML attributes, while Alpine.js manages lightweight client-side state like modals or dropdowns. Tailwind allows for rapid UI styling.
    *   *Constraints:* Relying heavily on HTMX means the frontend depends on the Flask server returning HTML fragments quickly. If the server experiences high latency, the UI will feel unresponsive.
*   **Backend: Python and Flask:**
    *   *Why:* Flask is highly modular, easy to set up for rapid prototyping, and integrates perfectly with the official Python SDKs needed for Gemini and Supabase.
    *   *Constraints:* Flask is synchronous by default. If the Gemini API takes several seconds to process a receipt image, it could temporarily block the server from handling other users' requests.
*   **Database: Supabase (PostgreSQL):**
    *   *Why:* Supabase is a powerful Backend-as-a-Service with a generous free tier. We will use the `supabase-py` Python client library to connect our Flask app for storing users, trips, and shared expenses.
    *   *Constraints:* Configuring Row Level Security (RLS) policies within Supabase can be complex but is strictly necessary to ensure users cannot access other groups' financial data.

**APIs & External Services:**
*   **Gemini Multimodal API:** Our core engine to parse uploaded receipt images into itemized, structured JSON data for the bill splitter. *Constraint:* We must write fallback logic in case the AI hallucinates or misreads a blurry price.
*   **Google Maps API:** Used for plotting collaborative locations and calculating routes. *Constraint:* Requires strict API key restrictions (HTTP referrers) in the Google Cloud Console to prevent quota theft.
*   **Geolocation API (Browser/Client):** Used to fetch the user's real-time coordinates to broadcast to the group map. *Constraint:* Requires explicit user permission, and battery drain can be an issue if polled too frequently.

**Hosting: Render.**
*   *Why:* Render offers a free tier for web services with seamless GitHub integration for automatic deployments.
*   *Constraints:* Render's free tier spins down the web service after 15 minutes of inactivity. This means the very first user to load the app after a period of rest will experience a "cold start" delay.

**Build plan & scope**
During the build phase, our scope will strictly focus on a Minimum Viable Product (MVP) to ensure realistic completion.
*What we will build:* A functioning Flask backend connected to Supabase for data persistence. A clean Tailwind/HTMX interface where users can create a trip, search and pin locations via the Maps API, test live location broadcasting, and upload a sample receipt to the Gemini API to demonstrate the automated expense splitting.
