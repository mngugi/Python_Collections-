def investigationMessage():
    print("Investgate Suspecious Activity")
application_status = "potential concern"
email_status = "OK!"

if application_status == "potential concern":
    print("application_log:")
    investigationMessage()
if email_status == "potential concern":
    print("email log:")
    dinvestigationMessage()
