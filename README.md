Justin Bates - Jujbates@ucsc.edu
Chris Egan - cjegan@ucsc.edu

SEE THE ONLINE VERSION!
https://manfrommars47.pythonanywhere.com/brainyape/

Project Description:
    Our project's proposal was to provide an easy and quick way to connect UC Santa Cruz tutors with tutees and vice versa. We wanted the user to be sucked in by our site's user interface, making it easy to find our tutor and student listings. One of the ways we made it easy for the user was to create a painless login and register. We choose to make the user log in via their UCSC google account. We then held the user's hand as we provide multiple pathways to our main features, the Tutor and Student listings. BrainyApe also provides a crash course on 'How to be a Tutor' for those user's that want to become entrepreneurs. As this web application might be simple we put a lot of time and took heavy yet friendly advice from friends and other fellow UCSC scholars.


Challenges:

-The biggest challenge we came across was being able to access web2py’s behind the scenes data bases to tweak data after it was already entered in. (auth_user)


		+ We created a profile form that would enter the information in a profile db, but thats not really what we wanted, we wanted the auth_user so we can link all the user data into one single db. 

		
		+Once we were able to link to the users auth_user db and update data to that auth_user db, that was a game changer. 


				> Ran into problems later with being able to create a stable link because we didnt want the users the have usernames. We wanted the site to be more personable. 


				> For that reason we had to create fields in the auth user for linking called ‘name’ and another called ‘fancy_name’. fancy_name being used to display the First name of user and last name of users. These were working at first for when we had just the profile db but after we found out how to not insert and not add but update the auth_user. 

-Other problems we had was trying to implement and emailing messaging system. we wanted a form to be a part of the viewing another users profile but just couldn’t figure that out. we left the code that we thought should of made it work in. So if its possible for an email on what was wrong with implementation because it worked for a day and then i think when we did our big db switch i think it might of messed it up or something. 

- We tried to run a plug-in like our other friends project but with a tutor rating scrubber bar but that wouldn’t work for some reason so we dropped it for a while and continued to work and do reading on what would help grab the users eye and make them think that we were better than the other guy. 

- We also tried to implement a search feature last minute where the students could search by only the following Major, College , Subject of tutors, on-off campus housing, and price of tutor but we didn't want to use the given web2py SQL Grid layout. We wanted it to have a more attractive look to the user’s eye to get them to come back to the site. So after struggling and not finding help from Web2py 


Challenges outside out code:

-Finding the right idea.

-Trying to find time to brainstorm and do a precoding stage where we take a step back and really look at what we want our user to be able to do and who we wanted the user to be. 
			> we choose to do implement features that would attract ucsc students looking to tutor and tutors that are looking to expand their business.


Goals: 

Our goal was to allow students to find tutors through a very simple interface. Students will be able to post classes they need a tutor for, while tutors will be able to post their schedule of availabilities. Once user is logged in and registers, with our easy login with goggle with a single button press, since we know our user would all have gmail(user@ucsc.edu)accounts. We wanted to user this as an opportunity to see the psychology behind the user habits and what drives the user back to a website. We found that color can catch the eye and give a higher probability of a users return to reuse this specific web app. 



List of features: 

Tutor listing
Student listing
Easy google log in
custom slideshow on homepage with 
self-profile viewing/ other-user profile viewing
>almost had messaging, super sad it stopped working (please email use if you can help with this bug, so we don't run into it and so we can keep finishing the project and implementing our dream features like the rate the tutor scrubber bar.

Github: https://github.com/ChrisEgan/budz
pythonanywhere: https://manfrommars47.pythonanywhere.com/brainyape/
(the two versions are slightly different, due to the directory names and janrain's functionality only being possible over a network connection.)
