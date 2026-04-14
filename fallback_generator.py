import random


class CaptionGenerator:

    CAPTIONS = {
        "linkedin": {
            "normal": [
                lambda t: f"✨Working on {t} today and making solid progress.It's not always glamorous — some days it's debugging, some days it's small wins. But every step forward counts, no matter how small.Showing up consistently is half the battle. The rest is just figuring it out as you go.#coding #developer #buildinpublic #softwareengineering #techcommunity",
                lambda t: f"💻Deep diving into {t} this week.It's one of those topics where the more you learn, the more you realize how much there is to explore. Some concepts click right away, others take a few tries — and that's completely fine.Learning something new every day keeps the momentum going. Slow and steady still beats standing still.#programming #techlife #developer #continuouslearning #buildinpublic",
                lambda t: f"🚀Spent the morning untangling {t}.Honestly, debugging can be frustrating — but there's something satisfying about finally tracking down the root cause. It's rarely where you expect it to be.Every bug teaches something, whether it's about the code, the system, or just how you approach problems. That's the mindset that keeps it from feeling like a waste of time.#coding #softwareengineering #growth #debugging #developerlife",
                lambda t: f"💻{t} is on my desk today.No shortcuts, no rushing — just breaking it down into smaller pieces and working through each one. It's easy to get overwhelmed looking at the big picture, so I try not to.Building projects step by step is the only way I know. And honestly, it's the only way that actually works.#developer #productivity #code #buildinpublic #softwareengineering",
                lambda t: f"🚀Making sense of {t} one commit at a time.Some days the progress feels invisible — small refactors, minor fixes, a bit of cleanup. But it all adds up more than you'd think.Coding my way to success — slowly but surely. There's no other way I'd rather do it.#programming #buildinpublic #techcommunity #developer #consistency",
            ],
            "professional": [
                lambda t: f"💻Currently advancing my expertise in {t}.The more you grow in this field, the more you realize how much still lies ahead. That used to feel daunting — now it just feels like motivation to keep goingContinuous learning is the cornerstone of engineering excellence. Sharing the journey with this community because growth rarely happens in isolation.#SoftwareEngineering #ProfessionalDevelopment #TechLeadership #ContinuousLearning #EngineeringCommunity",
                lambda t: f"🚀Invested in deepening my understanding of {t} this quarter.It's easy to jump between topics and never really go deep on anything. This time I wanted to do it differently — slower, more deliberate, actually sitting with the hard parts instead of skipping past them.Structured, incremental progress yields the most sustainable results in technical growth. No shortcuts, just consistent effort stacked over time.#EngineeringExcellence #ContinuousLearning #Developer #TechGrowth #Upskilling",
                lambda t: f"✨Exploring {t} as part of my ongoing skill development.It's not always a straight path — there are moments of confusion, dead ends, and having to start over. But that's kind of the point. You don't grow by only doing what's already comfortable.Every challenge encountered is an opportunity to refine both approach and craft. The more I lean into that, the better the process gets.#TechProfessional #GrowthMindset #SoftwareDevelopment #LearningEveryDay #Developer",
                lambda t: f"🚀Proud to share progress on {t}.It didn't come together overnight. There were iterations that didn't work, assumptions that had to be revisited, and moments of just sitting with the problem until something clicked.Systematic problem-solving and disciplined iteration are what separate good engineers from great ones. The willingness to go back, reassess, and improve — that's where the real growth happens.#Engineering #Leadership #CareerGrowth #SoftwareDevelopment #GrowthMindset",
                lambda t: f"💻Focused on mastering {t} to deliver higher-quality outcomes.Mastery isn't a destination — it's a standard you keep raising. The deeper you go into something, the more you notice the details that actually matter and the shortcuts that only look good on the surface.Professional excellence is built one well-considered decision at a time. Small, deliberate choices compound into something you can genuinely stand behind.#SoftwareEngineering #TechCommunity #ProfessionalGrowth #ContinuousImprovement #Developer",
            ],
            "funny": [
                lambda t: f"Me: I'll spend 20 minutes on {t}.\nAlso me, 4 hours later: still here.\n\nSend coffee. And maybe a search party.\n\n#developerlife #coding #sendhelpplease",
                lambda t: f"{t} said 'good luck' and walked out.\nI said 'I don't need luck, I have Stack Overflow.'\n\nWe both lied.\n\n#programmerhumor #developer #realstory",
                lambda t: f"Current status: arguing with {t} like it owes me money.\n\nIt does not. But it WILL work.\n\n#codinglife #programming #stubborndev",
                lambda t: f"Nobody:\nAbsolutely nobody:\nMe at 2am: maybe the issue with {t} is... wait.\n\nIT WAS A SEMICOLON.\n\n#devlife #coding #truestory",
                lambda t: f"{t} and I are in couples therapy.\n\nOur therapist is the documentation.\n\nIt's going okay.\n\n#developerhumor #techlife #programming",
            ],
        },

        "instagram": {
            "normal": [
                lambda t: f"✨Working on {t} today!!Some days it flows, some days it doesn't — but showing up regardless is what matters. Learning something new every day and loving every second of it.Drop a 🔥 if you're also deep in the code today.#coding #developer #programming #techlife #code #buildinpublic #learntocode #devlife #codeeveryday #softwaredev",
                lambda t: f"🔥Deep in {t} mode right now. 🔥distractions, just the problem in front of me and a lot of coffee. Some sessions just hit different.Building projects step by step — that's the vibe. One piece at a time until it all comes together. 🙌Anyone else in full focus mode today? 👇#coder #developer #buildinpublic #programming #100daysofcode #devlife #codeeveryday #learntocode #techlife #softwareengineering",
                lambda t: f"💻 {t} has been today's adventure!Spent way too long staring at one bug only to realize it was something small the whole time. Classic. 😅 But honestly that's part of the fun.Every bug teaches something. No complaints here — just better debugging skills and a lot of patience. 🙌What's been your biggest bug moment lately? Drop it below 👇#developer #coding #learntocode #techcommunity #code #devlife #buildinpublic #100daysofcode #codeeveryday #programminglife",
                lambda t: f"🚀 Making moves with {t}.It's not always pretty — there's plenty of trial, error, and Googling the same thing twice. But the progress is real and that's what keeps me going. 💪Coding my way to success one line at a time. Every line counts, even the ones you end up deleting. 😄What are you building right now? Let me know 👇#programming #coder #devlife #tech #developer #buildinpublic #100daysofcode #learntocode #codeeveryday #techlife",
                lambda t: f"✨ Leveling up with {t} today.Every time I sit down with something new, there's that moment of okay this is a lot — and then slowly it starts to make sense. That feeling never gets old. 🙌Small steps, big dreams. That's the energy. Consistency over perfection, always. 💫What are you leveling up on this week? 👇#coding #developer #growth #learntocode #buildinpublic #devlife #codeeveryday #techlife #100daysofcode #programminglife",
            ],
            "professional": [
                lambda t: f"Building expertise in {t} — one focused session at a time.\n\nGrowth is a daily practice, not a destination. 💡\n\n#ProfessionalDevelopment #TechGrowth #Developer #Coding #CareerGoals",
                lambda t: f"Dedicated today to mastering {t}.\n\nShowing up consistently is what makes the difference. Keep building. 🔧\n\n#CodeEveryDay #Developer #SoftwareEngineering #TechLife #LevelUp",
                lambda t: f"Progress report: {t} — checked.\n\nEvery skill built today compounds tomorrow. Stay disciplined. 🚀\n\n#TechProfessional #ContinuousLearning #Coding #Developer #Growth",
                lambda t: f"Deepening my understanding of {t} this week.\n\nExcellence isn't an event, it's a habit. Keep going. ✨\n\n#Engineering #CareerDevelopment #CodeLife #Programming #Mindset",
                lambda t: f"Another session of intentional practice — today's focus: {t}.\n\nStrong foundations make everything else possible. 💪\n\n#Developer #SkillBuilding #Programming #TechCommunity #100DaysOfCode",
            ],
            "funny": [
                lambda t: f"POV: you told yourself 'just a quick look' at {t} 🫠\n\n3 hours later. Still here.\n\n#developerlife #sendhelp #coding #programmers #relatable",
                lambda t: f"{t}: exists\nMe: I'll fix this in 5 mins\nAlso me: 🫠🫠🫠\n\nThis is fine. Everything is fine.\n\n#devhumor #coding #techlife #developerlife #lol",
                lambda t: f"My rubber duck after listening to me explain {t} for 2 hours: 🦆\n\nNo notes. It judges me silently.\n\n#rubberduckdebugging #developerlife #coding #techhumor #programmer",
                lambda t: f"Hot take: {t} is either the easiest thing in the world or the absolute hardest.\n\nThere is no in between. Zero.\n\n#programmer #coding #devlife #techhumor #mood",
                lambda t: f"Me explaining {t} to my non-tech friends 🧑‍💻\nThem: 👁️👄👁️\n\nAt least my cat seems interested.\n\n#developerlife #coding #relatable #techhumor #programmers",
            ],
        },

        "twitter": {
            "normal": [
                lambda t: f"Working on {t} today. Making progress, one step at a time.\n\n#coding #developer",
                lambda t: f"Spent the afternoon with {t}. Every session teaches something new.\n\n#programming #buildinpublic",
                lambda t: f"{t} on the agenda today. Keeping the momentum going.\n\n#code #developer #tech",
                lambda t: f"Deep in {t}. Bugs exist. Coffee helps.\n\n#developer #programming",
                lambda t: f"Logging off for the day after a solid session with {t}. Progress made. 💻\n\n#coding #buildinpublic",
            ],
            "professional": [
                lambda t: f"Investing time in {t} this week. Deliberate practice compounds fast.\n\n#SoftwareEngineering #Growth",
                lambda t: f"{t} — focused, structured, and making meaningful progress.\n\nThat's the approach.\n\n#Engineering #CareerDevelopment",
                lambda t: f"Continuous improvement in {t}. Discipline over motivation, always.\n\n#TechProfessional #Developer",
                lambda t: f"Another day building mastery in {t}. Small inputs, big outputs over time.\n\n#ContinuousLearning #SoftwareDev",
                lambda t: f"Committed to {t} this sprint. Intentional practice is the edge.\n\n#Engineering #TechGrowth #Developer",
            ],
            "funny": [
                lambda t: f"{t} said 'good morning' and immediately humbled me.\n\nI said thank you.\n\n#developerlife",
                lambda t: f"me: i understand {t}\n{t}: lol\n\n#programmers #coding",
                lambda t: f"every time i think i've figured out {t}, it reveals a new layer of chaos\n\nit's giving onion\n\n#devlife #techhumor",
                lambda t: f"'it's just a quick {t} task' — me, before losing 4 hours of my life\n\n#coding #sendhelp",
                lambda t: f"my relationship with {t} can be described as: it's complicated\n\nbut we're working on it\n\n#programmer #developerhumor",
            ],
        },
    }

    VALID_PLATFORMS = ("linkedin", "instagram", "twitter")
    VALID_TONES = ("normal", "professional", "funny")

    def generate_caption(self, details, platform: str = "linkedin", tone: str = "normal") -> str:
        """
        Generate a fallback caption.

        Args:
            details: object with a `.topic` attribute (string)
            platform: one of 'linkedin', 'instagram', 'twitter'
            tone:     one of 'normal', 'professional', 'funny'

        Returns:
            A formatted caption string.
        """
        platform = platform.lower().strip()
        tone = tone.lower().strip()

        if platform not in self.VALID_PLATFORMS:
            raise ValueError(f"Invalid platform '{platform}'. Choose from: {self.VALID_PLATFORMS}")
        if tone not in self.VALID_TONES:
            raise ValueError(f"Invalid tone '{tone}'. Choose from: {self.VALID_TONES}")

        options = self.CAPTIONS[platform][tone]
        caption_fn = random.choice(options)
        return caption_fn(details.topic)