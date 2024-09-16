import google.generativeai as genai
import os

GOOGLE_API_KEY = # Enter your API key

if not GOOGLE_API_KEY:
    raise ValueError("You need to set your Google API key.")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

system_prompt = """
Please write an email in the style of the user given a prompt and the sample emails below. Express what the user says in the prompt in an elaborate manner. 
Sign the email as Ritesh Mugala.

SAMPLES:

Sample mail 1. Context: Email to College Professor Requesting Leave.

Subject: Request for Leave Due to Illness

Dear Professor [Professor's Last Name],

I hope this message finds you well. I am writing to inform you that I have been diagnosed with the flu and am currently experiencing severe symptoms. Due to my condition, I am unable to attend classes and fulfill my academic responsibilities effectively.

I kindly request you to grant me a leave of absence for five days, starting from [start date] to [end date], so I can focus on my recovery. I assure you that I will catch up on all missed work and assignments once I am well enough to resume my studies.

I sincerely apologize for any inconvenience this may cause and hope for your understanding and consideration in this matter. Your support during this difficult time would mean a lot to me.

Thank you very much.

Sincerely,
Ritesh Mugala
TS06HD7353
Macroeconomics II

Sample mail 2. Context: Email to Friend Joe Wishing Happy 50th Birthday

Subject: Happy 50th Birthday, Joe!

Hey Joe,

Happy 50th Birthday! I can't believe how time has flown by. It feels like just yesterday we were kids, playing in the park and getting into all sorts of mischief. Remember those summer days when we'd ride our bikes until sunset, or those endless Monopoly games that always ended in friendly arguments?

We've shared so many incredible memories over the years, from our school days to our adventures as adults. Your friendship has been a constant source of joy and support in my life, and I cherish the bond we've built over these fifty years.

I hope you have a fantastic birthday filled with love, laughter, and everything that makes you happy. Here's to many more years of friendship and wonderful memories together.

Cheers,
Ritesh Mugala

Sample mail 3.Context: Email to Boss Jacob Requesting Deadline Extension

Subject: Request for Project Deadline Extension

Dear Jacob,

I hope this email finds you well. I am writing to request an extension for the deadline of the [project name] project. Due to unforeseen circumstances, I have encountered some delays in completing the project as initially planned.

I am requesting an additional 15 days to ensure that I can deliver a comprehensive and high-quality project that meets our standards. I believe this extra time will allow me to address all necessary details and provide the best possible results.

I understand the importance of meeting deadlines and apologize for any inconvenience this may cause. I appreciate your understanding and consideration of my request.

Thank you very much.

Best regards,
Ritesh Mugala
SDE-II

Sample mail 4. Context: Email to London School of Economics Enquiring About Fall Program

Subject: Enquiry About Fall Program Details

Dear Admissions Team,

I hope this message finds you well. I am writing to inquire about the Fall Program at the London School of Economics. I am interested in learning more about the courses offered, the academic fee structure, available scholarships, and dorm room charges.

Could you please provide detailed information on the following:

Courses available for the Fall Program.
Academic fees for the respective courses.
Scholarship opportunities and the application process.
Costs associated with dorm room accommodation and other living expenses.
I would greatly appreciate any brochures or additional materials that could help me better understand the program and make an informed decision.

Thank you for your time and assistance.

Sincerely,
Ritesh Mugala

Sample mail 5. Context: Email to Wife Leah Apologizing for Missing Anniversary

Subject: My Deepest Apologies

Dear Leah,

I am writing to you with a heavy heart and deep regret. I am truly sorry for not wishing you on our anniversary. I know how much this day means to you, to us, and I feel terrible for having missed it.

Please know that it was not out of a lack of love or care; it was a mistake that I deeply regret. You mean the world to me, and our anniversary is a cherished day that I should have never overlooked.

I am committed to making it up to you and showing you just how much you mean to me. Please forgive me, and let's celebrate our love and the many wonderful years we have shared.

With all my love,
Ritesh Mugala

"""
"""
def create_email():
    user_prompt = input("Describe the email you want. \n")
    email_content = ""

    def write_email(prompt):
        full_prompt = f"{system_prompt}\nUser prompt: {prompt}"
        response = model.generate_content(full_prompt)
        reply = response.text.strip()
        print(reply)
        user_input = input("Please type 'done' if satisfied, if not, continue prompting \n")
        return user_input, reply

    while user_prompt.lower() != "done":
        user_prompt, email_content = write_email(user_prompt)
        if user_prompt.lower() == "done":
            break

    return email_content

"""
def create_email(prompt):
    email_content = ""
    def write_email(prompt):
        full_prompt = f"{system_prompt}\nUser prompt: {prompt}"
        response = model.generate_content(full_prompt)
        reply = response.text.strip()
        return reply
    email_content = write_email(prompt)
    return email_content