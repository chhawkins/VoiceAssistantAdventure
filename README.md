# VoiceAssistantAdventure
<h3>
Have you ever wanted to play D&D but your the only one around?
Have no fear, Voice Assistant Adventure is here! 
</h3>

This githb hosts the source code for the web server and game of our Alexa Skill
Voice Assistant Adventure. All files withen VoiceAssistantAdventure 
(exlcuding ones defined in .gcloudignore) are uploaded to the Google Cloud Platform.
Specifically a Google App Engine instance using the command:
<b>gcloud app deplot</b> while in the base folder VoiceAssistantAdventure.

One thing not clear from code available here is that the Alexa Skill
sends its HTTP SSL requests to a registered Domain that is then picked up by
the Gunicorn agent which begins running the main script here.