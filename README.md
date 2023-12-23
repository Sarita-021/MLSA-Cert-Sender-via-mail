# MLSA-Cert-Sender-via-mail

This repo send certificate to participants of MLSA event on their mail Id's. Further, this repo can be futher modified according to your needs.

##  For Windows and Mac users.

## Caution ‼️

### Create a separate gmail id for his purpose to avoid any kind of problem.
   - Since this process requires your gmail id password and by chance your code get published on net or you give someone else your laptop
     with your repo left open then there are chances that your password got leaked and misused by someone else or even got hacked. So be careful while using.

## Customize your gmail account 

1. Make sure you have turned on 2 step verification.
   - To turn on 2 step veriication you can head over to your web browser and find there steps of how to turn on 2 step verification of your gmail account (you can easily find it.
  
2. Head over to 2 Step Verification section and follow the steps.

3. Scroll down to the App password and click on it.
   <br>
   <img width="500" alt="S1" src="https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/assets/121181405/638f1a28-322c-42c4-b175-dcb6014ec10f">

4. Create a new App Password and copy the 16 Character code which will be visible
   on your screen since you will be using that as your gmail password.

   <br>
   <img width="500" alt="S2" src="https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/assets/121181405/aeaea863-4b04-481b-af81-7ace7ecf21d5">


## Run these commands in your terminal

```
git clone https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/
cd MLSA-Cert-Sender-via-mail
```

## Customization and Generation

### Step 1 : Adding list of participants and their gmail ID.

<br>

<img width="500" alt="S3" src="https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/assets/121181405/4eac91e9-c316-4a0c-92c8-4799fce87757">


- Now Copy the name of Participants and their respective mail ID's from your list and paste their details in the file  `data.csv` file present in the folder `Data`.
- Save the changes
- No additional field required

### Step 2 : Add pdf of their certificates in pdf folder present in the `Data` folder.
   📌 Note :- Take care that name of pdf's should be same as that of the participants otherwise an error message will be shown in terminal.

### Step 3 : Modifying your event details

<br>

<img width="500" alt="S4" src="https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/assets/121181405/d9c9fd2b-05a0-4454-8e90-4d78e84e5528">


- Open the file `send-mail.py`
- Move to line 58 and Write "Host Gmail ID" instead of "hostgmail@gmail.com"
- Move to line 61 and Write name of the "Host" instead of "Your Name"
- Move to line 64 and Write your "Gmail ID password" instead of "Your GmailID Password" (if not working then enter thet `16-Character code` which you have copied above.
- Move to line 67 and Write your "Event name" instead of "Your Event Name"
- Save the changes.

### Step 4 : Open Terminal

### ```For Mac Users```

```
pip3 install -r requirements.txt
python3 send-mail.py
```

### ```For Windows Users```

```
pip install -r requirements.txt
python send-mail.py
```

### Step 4 : Verificatin 

- In console you will be able to see the list of all the participants with the messages displayed as `Mail send to //Participant_Name` who have received the mail.

## Here's how your mail look like

![S5-Gmail](https://github.com/Sarita-021/MLSA-Cert-Sender-via-mail/assets/121181405/8e41ff88-de08-409b-8f44-2ecdc1a7ac19)

<br>
# Well Done!!! You Did It.
# Thank You
