import webbrowser
import pywhatkit


class BrowserAgent:

    def respond(self, message: str):

        message = message.lower()

        # ---------- OPEN WEBSITES ----------
        if "open youtube" in message:
            webbrowser.open("https://youtube.com")
            return "Opened YouTube"

        if "open google" in message:
            webbrowser.open("https://google.com")
            return "Opened Google"

        if "open github" in message:
            webbrowser.open("https://github.com")
            return "Opened GitHub"

        # ---------- SEARCH ----------
        if "search" in message:
            query = message.replace("search", "").strip()
            pywhatkit.search(query)
            return f"Searching for: {query}"

        return "Browser task not recognized"