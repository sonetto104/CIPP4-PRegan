
# PianoPhiles

![Preview of PianoPhiles](/static/assets/img/amiresponsive-mockup.png)

**Live Site:**

[Live webpage](https://pianophiles-cbf072093775.herokuapp.com/)

**Link to Repository:**

[Repository](https://github.com/sonetto104/CIPP4-PRegan)

**Developed by: Peter Regan**

## Table of Content TO GO HERE

## Introduction

PianoPhiles is a blog site for piano lovers where they can share clips of their favourite performances, post questions about technique or interpretation, or share pictures of their fun piano moments. As well as being able to share content in text, image and video format, users can discuss the material with other likeminded keyboard enthusiasts through comments, show their appreciation with likes and add a personal touch to their own profile page with a short bio and profile photo. Let's get tinkling those keys!

The site was built in fulfilment of the requirements for Portfolio Project 4 of Code Institute's Diploma in Full Stack Software Development. It was built using Django, Python, JS, CSS, and HTML. The site data is stored in a PostgreSQL database.

#### Database Schema

The project utilizes PostgreSQL as the database technology of choice with psycopg2 as the PostgreSQL adapter for Python. Additionally, the project leverages the dj-database-url package, which facilitates the handling and parsing of database URLs. This allows for seamless configuration of the database connection using a URL format specified by the PostgreSQL provider. By utilizing these database technologies, the project ensures efficient and secure data storage and retrieval, enabling robust and scalable web application functionality.

Here is an overview of the most important data relationships in the project.

## ERD Diagram

| Model        | Fields                                         | Relationships                            |
|--------------|------------------------------------------------|------------------------------------------|
| User         | id, username, email, password, ...              |                                          |
| Profile      | id, owner_id, created_on, updated_on, bio, ...  | owner (OneToOne with User)                |
| Post         | id, title, slug, author_id, created_on, ...     | author (ForeignKey to User)               |
|              |                                                | likes (ManyToMany with User)              |
| TextPost     | content                                        | parent: Post                             |
| ImagePost    | image                                          | parent: Post                             |
| VideoPost    | video                                          | parent: Post                             |
| PostComment  | id, post_id, author_id, content, ...            | post (ForeignKey to Post)                |
|              |                                                | author (ForeignKey to User)               |

## User Experience - UX

The project was developed considering the Five Planes of User Experience: Strategy, Scope, Structure, Skeleton and Surface.

### Strategy

| EPIC                       | ID  | User Story                                                                                                                                                                               |
| -------------------------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CONTENT AND NAVIGATION** |     |                                                                                                                                                                                          |
|                            | 1A  | As a user, I want to be able to easily navigate through the content available on the site.                                                                                                        |
|                            | 1B  | As a user, I want to see relevant information about the site and its content easily so I can decide if I want to register an account                                                     |
|                            | 1C  | As a user, I want the design of the site to be simple, intuitive and appealing.                                                                               |
|                            | 1D  | As a user, I want to be able to access different areas of the site e.g. detailed blog posts, or user profiles with ease so that I may easily enjoy the feautures the site has to offer.                                                          |
| **REGISTRATION AND USER INFORMATION**  |     |                                                                                                                                                                                          |
|                            | 2A  | As a user, I want to create my own profile, so I have a familiar and comfortable place where I can share my enthusiasm for piano and keep track of discussions, as well as accessing all the functionality the site has to offer.                                             |
|                            | 2B  |  As a user, I want to be able to edit my profile so that it reflects me as I change.                                                                                           |
|                            | 2C | As a user, I want to be able to log into my account easily, so I can access my account information.                                                                                      |
|                            | 2D  | As a user, I want to be able to log out of my account with ease to protect my account information.                                                                                       |
|                            | 2E  | As a user, I want to be able to delete my account information/profile if I feel the site community no longer reflects my values.                                                                      |
|                            | 2F | As a user, I also want the option of being able to use the site passively without registering an account, even if this means I can't access some site functionality like making posts or comments.                                                                             |
| **MANAGING POSTS AND COMMENTS**   |     |                                                                                                                                                                                          |
|                            | 3A  | As an authenticated user, I want to be able to create text posts so that I can share my enthusiasm with my online community.     |
|                            | 3B   | As an authenticated user, I want to be able to create image posts so that I can share my enthusiasm with my online community.     |
|                            | 3C  | As an authenticated user, I want to be able to create video posts so that I can share my enthusiasm with my online community.     |
|                            | 3D  | As an authenticated user, I want to be able to delete my posts if I feel they no longer reflect my opinions.                                                                 |
|                            | 3E  | As an authenticated user, I want to be able to comment on other users' posts in order to encourage discussion and a sense of community.                                     |
|                            | 3F  | As an authenticated user, I want to be able to delete my past comments if I feel they no longer reflect my opinions.   |
|                            | 3G  | As an authenticated user, I want to be able to "like" posts in order to show appreciation.   |
| **USER VIEWS**             |     |                                                                                                                                                                                          |
|                            | 4A  | As a user, I want to be able to see all publicly available posts so that I can browse through them.                                                                              |
|                            | 4B  | As a user, I want to be able to view the detail of all publicly available posts, so I can read the full content associated with them, including comments.                             |
|                            | 4C  | As a user, I want to be able to view the record of a given user's publicly available posts and comments.                                   |
|                            | 4D  | As an authenticated user, I want to be able to view a record of all my publicly available posts.  |
|                            | 4E  | As an authenticated user, I want to be able to view a record of all my publicly available comments. |

**Site Goal**

  The goal of the site is to create a place where piano lovers can really sink their teeth into their favourite arguments about the art. Spaces like pianostreet and pianoworld have continued to be steadily active throughout the lifespan of widespread popular internet usage, but their UX and site design has hardly changed at all over more than 20 years. It would be nice to host these discussions somewhere with a much more appealing, simple and intuitive interface.

**Target Audience**

  Users of the site are likely to be advanced second level and conservatoire level student pianists, and enthusiastic amateur pianists; a reflection of the real life piano recital going audience.

### Scope

**Simple User Experience**

- Must Have
The project must have:
    - A home page displaying new posts related to the piano.
    - Login/logout functionality allowing users to maintain anonymity if they so choose.
    - Commenting functinonality so that users can discuss their views.
    - A database that stores user data securely.
    - Video hosting capability.
    - Text hosting capability.
    - Image hosting capability.

- Should Have

    - Profile functionality where users can choose whether or not to share information about themselves, and where they can access their history of activity notifications etc.
    - Ability to like posts.
    - Dynamic like button.

- Could Have
    - Live chat feature.
    - Different genres for classical, jazz and pop.
    - Search functionality.
    - Tag functionality so users can search by tags, keywords or genre.

**Relevant Content**

- Concise information should be visible immediately making the site's purpose clear.
- User generated content should be the primary focus of the site and should be immediately visible on landing, further enhancing the user's understanding of the site's purpose in an intuitive way.

### Structure

The site has 16 pages depending on whether the user is authenticated/logged-in or not.

  - **Home** This is the landing page. Here the user can see the site's most recently posted content. It indicates the site's purpose as a piano lover's blog and allows the user to visit the login or registration page.

  - **Post Detail** Each post has its own page displaying the full content of the post (as opposed to the post preview on the home page which displays only the title, image/video if applicable, and the first two comments).

  - **Profile** Every authenticated user has a profile page displaying their username, date of joining, short biography section and a profile picture. It also displays their most recent posts and comments. All users who do not wish to upload a profile photo are given an automatic sample profile photo.

  - **Edit Profile** A logged in authenticated user can edit/update their previously exisiting profile information and profile photo using the "Edit Profile" form.

  - **View All User Posts Page** When visiting a user's profile, there is the option to view all the publicly available posts of that user, whether the visitor is an authenticated user or not.

  - **View All Comments** Similarly to being able to view all of a user's posts, one can view all of a user's publicly available comments in one page.

  - **Delete Post** A logged in authenticated user can delete posts belonging to them.

  - **Delete Comment** A logged in authenticated user can delete comments belonging to them.

  - **Delete Profile** All logged in authenticated users have the option to fully delete their profile and information, including associated posts and comments.

  - **Create Post** The create post page brings users to a page with links to forms allowing them to create either image, video or text posts.

  - **Create Image Post** This is a form allowing a logged in authenticated user to create a post specifically centered around an image.

  - **Create Video Post** This is a form allowing a logged in authenticated user to create a post specifically centered around a video clip.

  - **Create Text Post** This is a form allowing a logged in authenticated user to create a post containing only text.

  - **Sign In** There is a sign in page allowing authenticated users to log in and access the CRUD functionality associated with their profile.

  - **Sign Out** Logged in authenticated users can log out of their account to protect their information on foreign devices.

  - **Register** Non authenticated users can create an account through the registration form.

  - **Custom 404 Page** If a user tries to access a url path that doesn't exist, a custom 404 error page is provided.


### Skeleton Plane

As per the requirements of Code Institute's Portfolio Project 4 assignment, this functions at the most basic level as a CRUD application.

C - Users can create profiles, comments and posts.
R - Users can read the profiles, comments and posts of other users. They can read their own comments and posts.
U - Users can edit their profiles.
D - Users can delete their past comments, posts and their profile.

#### Site Flow

Most of the site should flow centrally from the home page. I used Lucid Chart to make a diagram with a rough outline of how the site should flow.

<details>
<summary>Site Flow Diagram</summary>
<img src="https://res.cloudinary.com/dayngkoud/image/upload/v1688981726/static/assets/img/pianophiles-siteflow.d43094cb9385.jpg" width="80%">
</details>


#### Wireframes

I used Figma to make these basic wireframes for how I imagined the website would look.

#### Sample Home Page Layout

<details>
<summary>Sample Home Page Layout</summary>
<img src="https://res.cloudinary.com/dayngkoud/image/upload/v1693998827/static/assets/img/pianophiles-homepage.42d9905736ef.jpg" width="80%">
</details>

#### Sample Profile Layout

<details>
<summary>Sample Profile Layout</summary>
<img src="https://res.cloudinary.com/dayngkoud/image/upload/v1688982739/static/assets/img/android-small.ff428050db13.jpg" width="80%">
</details>

#### Sample Login Page Layout
<details>
<summary>Sample Login Page Layout</summary>
<img src="https://res.cloudinary.com/dayngkoud/image/upload/v1688982739/static/assets/img/android-small-page-1.b5234329fa21.jpg" width="80%">
</details>


#### Sample Post Page Layout
<details>
<summary>Sample Post Page Layout</summary>
<img src="https://res.cloudinary.com/dayngkoud/image/upload/v1688982740/static/assets/img/android-small-page-2.04e4f7e2bdba.jpg" width="80%">
</details>


### Surface

#### Colour Scheme

The colours used in the site are primarily white, red and black. These colours were chosen in the interest of legibility, and not to distract from or contrast too strongly with the content of image and video posts. There are some instances of blue where buttons are responsible for CRUD operations related to authenticated user information. The "delete profile" button is the only other outlier in the whole site - it is yellow and black. It is designed to stand out as it is responsible for a significant irreversible action.

From a creative perspective, whiite and black are reminiscent of piano keys and create a visually cohesive and elegant design, immediately conveying the central theme of the blog. The addition of red infuses energy and accentuates key elements, such as buttons, providing a subtle but effective visual contrast. 

Overall, this colour scheme not only pays homage to the piano's iconic palette but also ensures a user-friendly and aesthetically pleasing reading experience for visitors interested in piano-related content.

![PianoPhiles Colour Scheme](/static/assets/img/pianophiles-scheme.png)


### Manual Testing

| Test Case                         | Description                                                                                                                   | Expected Outcome                                   | Pass/Fail |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|-----------|
| User Registration                | Test the registration process by creating a new user profile.                                                                 | User is able to successfully register and is redirected to the home page.                          |  Pass         |
| User Login                       | Test the login functionality by logging in with a registered user account.                                                    | User is able to log in and is redirected to the home page.                                          | Pass   |
| Create a Post                    | Test the ability to create a new post by a logged-in user.                                                                     | Post is successfully created and displayed on the home page.                                       |    Pass       |
| View Recent Posts                | Test the display of recent posts on the home page.                                                                             | Recent posts are displayed correctly on the home page.                                              |    Pass       |
| Comment on a Post                | Test the ability to add a comment on a post.                                                                                   | Comment is successfully added to the post and displayed.                                           |    Pass       |
| View User's Profile              | Test the display of a user's profile page.                                                                                    | User's profile page is displayed correctly with the relevant information.                          |    Pass       |
| Edit User's Profile              | Test the ability to edit the user's profile information.                                                                      | User's profile information is successfully updated.                                               |  Pass         |
| Delete a Post                    | Test the ability to delete a post created by the user.                                                                         | Post is successfully deleted and no longer displayed on the site.                                  |      Pass     |
| Delete a Comment                 | Test the ability to delete a comment made by the user.                                                                         | Comment is successfully deleted and no longer displayed on the post.                               |      Pass     |
| Like a Post                      | Test the ability to like a post.                                                                                              | Post is successfully liked by the user.                                                            |     Pass - can be improved      |
| Logout                           | Test the logout functionality by logging out from a user account.                                                            | User is logged out and redirected to the login page.                                               |      Pass     |
| View Posts of Other Users        | Test the ability to view posts made by other users.                                                                            | Posts made by other users are displayed correctly.                                                 |  Pass         |
| Delete User's Profile            | Test the ability to delete the user's profile.                                                                                 | User's profile is successfully deleted, and all associated data is removed.                        |    Pass       |
| View the Site without Logging In | Test the ability to access the site and view content without logging in.                                                      | User can access and view the site's content without logging in.                                   |     Pass      |
| Dynamic Like Button              | Test the behavior of the dynamic like button on a post.                                                                        | Like button updates and reflects the user's liking/unliking of a post.                            |    Pass - can be improved - not fully dynamic as it acts as a redirect.       |
| Search Functionality             | Test the search functionality to search for posts based on keywords or tags.                                                  | Search results display relevant posts based on the search query.                                  |    Fail       |
| Tag Functionality                | Test the ability to assign tags to posts and filter posts by tags.                                                            | Posts can be assigned tags, and filtering by tags displays relevant posts.                        |     Fail      |
| Live Chat Feature                | Test the functionality of the live chat feature, if implemented.                                                              | Live chat feature functions as expected, allowing real-time communication between users.          |    Fail       |
| Ability to Delete Previous Posts and Comments | Test the ability to delete previous posts and comments made by the user.                                               | User's previous posts and comments are successfully deleted.                                       |  Pass         |


### Deployment

1. Set up a Heroku account:

- Go to the Heroku website (https://www.heroku.com/) and sign up for a new account if you don't have one already.
Install the Heroku CLI:

- Download and install the Heroku CLI (Command Line Interface) based on your operating system. You can find the installation instructions on the Heroku website.

2. Set up your Django project on GitHub:

- Make sure your Django project is hosted on a GitHub repository. If not, create a new repository for your project and push your code to it.

3. Create a new Heroku app:

- Log in to your Heroku account.
From the Heroku dashboard, click on the "New" button and select "Create new app".
Give your app a unique name, choose the region, and click on the "Create app" button.
Connect your GitHub repository to Heroku:

4. In the "Deployment method" section of your Heroku app dashboard, select the "GitHub" option.
Search for your repository name and click on the "Connect" button to connect your GitHub repository to Heroku.
Configure environment variables:

5. In the "Settings" tab of your Heroku app dashboard, click on the "Reveal Config Vars" button.
Add any necessary environment variables your Django project requires (e.g., SECRET_KEY, DATABASE_URL, etc.).
If using Cloudinary for hosting static files, include the necessary Cloudinary environment variables (e.g., CLOUDINARY_URL, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, etc.).
Set up the PostgreSQL database:

6. In the "Resources" tab of your Heroku app dashboard, search for "Heroku Postgres" in the "Add-ons" section and select the plan that suits your needs.
Once the Postgres add-on is provisioned, you can access the database credentials in the "Settings" tab under the "Config Vars" section.

7. Create a Procfile:

- In your Django project's root directory, create a file named "Procfile" (without any file extension) and add the following line:

"web: gunicorn your_project_name.wsgi --log-file"

8. Replace "your_project_name" with the actual name of your Django project.
Install necessary dependencies:

- Make sure your Django project's dependencies are listed in a requirements.txt file. You can generate this file using the command pip freeze > requirements.txt in your project's virtual environment.

9. Configure static files and Cloudinary:

- Install the necessary packages for Cloudinary integration, such as cloudinary and dj3-cloudinary-storage.
In your Django project's settings.py file:

10. Set STATIC_URL = '/static/' to define the URL for serving static files.
- Set STATICFILES_STORAGE to use Cloudinary for storing static files. Use the value 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'.
- Set DEFAULT_FILE_STORAGE to use Cloudinary for storing uploaded media files. Use the value 'cloudinary_storage.storage.MediaCloudinaryStorage'.
- Make sure CLOUDINARY_URL, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET, and other necessary Cloudinary environment variables are correctly configured.

11. Configure Debug and static file collection settings:

- In your Django project's settings.py file:
- Set DEBUG = False to disable debug mode in production.
- Set DISABLE_COLLECTSTATIC = 1 to prevent Heroku from running the collectstatic command during deployment. This is  important because static files are already being handled by Cloudinary and don't need to be collected.

12. Commit and push changes:

- Make sure all your changes, including the Procfile, requirements.txt, and updated settings.py file, are committed and pushed to your GitHub repository.
Deploy your app on Heroku:

13. In the "Deploy" tab of your Heroku app dashboard, scroll down to the "Manual deploy" section. You can enable automatic deployments for every time you push your code.
- Click on the "Deploy Branch" button to deploy your app from the GitHub repository.
Monitor the deployment:

- Once the deployment is initiated, you can monitor the build progress in the "Activity" tab of your Heroku app dashboard.
- If the build process encounters any errors, you can check the logs by clicking on the "View Logs" button.
Verify your deployed app:

14. After a successful deployment, Heroku will provide you with the URL of your app.
Open the URL in your browser to verify that your Django app is running correctly on Heroku.
Check if static files are being served properly and if Cloudinary is being used for hosting and retrieving static files.
- Your Django app should now be deployed and running on Heroku, with static files being served from Cloudinary. 


### Technologies Used

- [asgiref](https://pypi.org/project/asgiref/) - Version 3.7.2
  - ASGI (Asynchronous Server Gateway Interface) implementation for Django, providing compatibility with async frameworks.

- [backports.zoneinfo](https://pypi.org/project/backports.zoneinfo/) - Version 0.2.1 (for Python versions prior to 3.9)
  - Backport of the "zoneinfo" module introduced in Python 3.9, providing support for IANA time zones.

- [cloudinary](https://cloudinary.com/documentation) - Version 1.33.0
  - Cloud-based media management platform for storing, managing, and delivering images and videos.

- [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/) - Version 0.7
  - Integration of Django forms with Bootstrap 5, providing easy form rendering and customization.

- [dj-database-url](https://pypi.org/project/dj-database-url/) - Version 2.0.0
  - Allows configuring the Django database connection using a URL, simplifying database configuration.

- [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Version 0.0.6
  - Provides a storage backend for Django to interact with Cloudinary for file and media storage.

- [Django](https://docs.djangoproject.com/) - Version 3.2.19
  - A high-level Python web framework for building robust and scalable web applications.

- [django-allauth](https://django-allauth.readthedocs.io/) - Version 0.54.0
  - Enables user authentication and registration with support for multiple social accounts.

- [django-bootstrap-pagination](https://pypi.org/project/django-bootstrap-pagination/) - Version 1.7.1
  - Adds pagination support to Django projects, with Bootstrap-themed pagination templates.

- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/) - Version 2.0
  - Helps in rendering Django forms in a visually appealing way by integrating with Bootstrap.

- [django-pagination](https://pypi.org/project/django-pagination/) - Version 1.0.7
  - Provides easy pagination of Django querysets with support for various paginators.

- [django-simple-pagination](https://pypi.org/project/django-simple-pagination/) - Version 1.3
  - Offers simple pagination for Django projects without relying on database-specific functionality.

- [django-summernote](https://django-summernote.readthedocs.io/) - Version 0.8.20.0
  - Integration of the Summernote WYSIWYG editor with Django for rich text editing capabilities.

- [gunicorn](https://gunicorn.org/) - Version 20.1.0
  - A Python WSGI HTTP server that acts as a gateway between web applications and HTTP servers.

- [oauthlib](https://oauthlib.readthedocs.io/) - Version 3.2.2
  - Provides a generic implementation of the OAuth 1.0 and OAuth 2.0 specifications for Python.

- [Pillow](https://pillow.readthedocs.io/) - Version 9.5.0
  - A powerful Python imaging library for image processing and manipulation.

- [psycopg2](https://pypi.org/project/psycopg2/) - Version 2.9.6
  - PostgreSQL adapter for Python, allowing Django to interact with PostgreSQL databases.

- [PyJWT](https://pyjwt.readthedocs.io/) - Version 2.7.0
  - Provides JSON Web Token (JWT) implementation in Python, useful for authentication and authorization.

- [python3-openid](https://pypi.org/project/python3-openid/) - Version 3.2.0
  - Python library for working with OpenID authentication.

- [pytz](https://pypi.org/project/pytz/) - Version 2023.3
  - Python library for dealing with time zones, including localization and conversion.

- [requests-oauthlib](https://requests-oauthlib.readthedocs.io/) - Version 1.3.1
  - Provides OAuth client support for making authenticated requests using the OAuth protocol.

- [sqlparse](https://pypi.org/project/sqlparse/) - Version 0.4.4
  - A non-validating SQL parser for Python, useful for formatting and analyzing SQL statements.

- [urllib3](https://urllib3.readthedocs.io/) - Version 1.26.16
  - A powerful HTTP client library for Python, providing connection pooling and request functionality.




### Acknowledgements

Several of the Class based models and their associated functions were taken directly from or modeled on the code used in Code Institute's Codestar Blog project.

Tips on pagination came from this website: https://realpython.com/django-pagination/#using-the-django-paginator-in-views

Advice on having issues with getting Cloudinary to serve static files correctly to Heroku were taken from several Stack Overflow posts - https://stackoverflow.com/questions/72837010/cannot-push-to-heroku-with-cloudinary-storing-my-staticfiles

https://stackoverflow.com/questions/70231804/how-can-i-upload-all-types-of-files-videos-audios-pdfs-zip-in-cloudinary-in

YouTube tutorials on Cloudinary and Django: https://www.youtube.com/watch?v=fQo9ivqX4xs
https://www.youtube.com/watch?v=i0ar7W98Osc

Article on editing the Summernote editor: https://djangocentral.com/integrating-summernote-in-django/



















  

