
# PianoPhiles

![Preview of PianoPhiles](/static/assets/img/amiresponsive-mockup.png)

**Live Site:**

[Live webpage](https://pianophiles-cbf072093775.herokuapp.com/)

**Link to Repository:**

[Repository](https://github.com/sonetto104/CIPP4-PRegan)

**Developed by: Peter Regan**

## Table of Contents

- [PianoPhiles](#pianophiles)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Database Schema](#database-schema)
  - [ERD Diagram](#erd-diagram)
  - [User Experience - UX](#user-experience---ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Agile Development](#agile-development-for-pianophiles)
  - [Testing and Validation](#testing-and-validation)
  - [Deployment](#deployment)
  - [Technologies Used](#technologies-used)
  - [Bugs and Future Features](#bugs-and-future-features)
  - [Acknowledgements](#acknowledgements)

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


### Skeleton

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

From a creative perspective, white and black are reminiscent of piano keys and create a visually cohesive and elegant design, immediately conveying the central theme of the blog. The addition of red infuses energy and accentuates key elements, such as buttons, providing a subtle but effective visual contrast. 

Overall, this colour scheme not only pays homage to the piano's iconic palette but also ensures a user-friendly and aesthetically pleasing reading experience for visitors interested in piano-related content.

<br><br>

![PianoPhiles Colour Scheme](/static/assets/img/pianophiles-scheme.png)

<br><br>

#### Font

I decided not to customise font for PianoPhiles and chose to stick with Bootstrap's standard typography. It is easily legible and light, allowing the user's focus to be primarily on the content of posts rather than design elements.

<br><br>

![Fonts in Action](/static/assets/img/fonts-sample.png)

<br><br>

#### Logo

The logo and favicon were created using Figma. It is minimal, reflecting the simplicity of the site, using a splash of red to embody the sense of engagement I hope the site can spark, and plays on the heart shape of a grand piano. This ties into the site name, PianoPhiles, which not only means "piano lovers", but also plays on the idea of "piano files" suggesting a store where one can find all sorts of documents relating to the subject.

![PianoPhiles Logo](/static/assets/img/piano-philes-logo.png)

### Views


#### Home Page View

The home page view displays the site logo, nav bar and the site's most recently published posts. If the user is not logged in the nav bar offers the option to visit the homepage, register an account or sign in, and if the user is logged in, it offers the option to visit the home page, visit your own profile or logout.

<br><br>

- **Home Page Not Logged In**
<br><br>

![Home Page View Not Logged In](/static/assets/img/homepage-view-not-logged-in.png)

<br><br>

- **Home Page Logged In**
<br><br>

![Home Page View Logged In](/static/assets/img/home-page-logged-in.png)

<br><br>

#### Profile View

All users' profiles can be viewed on the site, whether the user viewing the profile is logged in or not. If a logged in user is viewing their own profile, they have the option to edit their profile or to delete their past posts or comments.

<br><br>

- **Profile Page Not Logged In**

![Profile View Not Logged In One](/static/assets/img/profile-view-not-logged-in.png)

<br><br>

![Profile View Not Logged In Two](/static/assets/img/profile-view-not-logged-in-two.png)

<br><br>

![Profile View Not Logged In Three](/static/assets/img/profile-view-not-logged-in-three.png)

<br><br>

- **Profile Page Logged In**

![Profile View Logged In One](/static/assets/img/my-profile-view.png)

<br><br>

![Profile View Logged In Two](/static/assets/img/profile-view-logged-in.png)

<br><br>

![Profile View Logged In Three](/static/assets/img/profile-view-logged-in-delete-button.png)

<br><br>


#### Post Detail View

Upon clicking any post, a user will be redirected to a more detailed version of the post, displaying the date of its publication, its author, the full post content (which is not available in previews of text posts) and all its associated comments. Only slices of the first two comments are available in post previews.

<br><br>

- **Post Detail View and Comments**

![Post Detail View](/static/assets/img/post-detail-view-not-logged-in.png)

<br><br>

![Post Detail View With Comments](/static/assets/img/comments-post-view-not-logged-in.png)

<br><br>

#### Sign In and Sign Out Pages

Some light customisation was added to allauth's generic sign in and sign out templates that were used for the site.

- **Sign In**

![Sign In](/static/assets/img/sign-in.png)

<br><br>

- **Sign Out**

![Sign Out](/static/assets/img/signout-view.png)

#### CRUD Functionality and Associated Views

The site's full CRUD operations are only available to authenticated logged in users. These include:
1. Creating a profile.
2. Editing a profile.
3. Deleting a profile.
4. Creating a text post.
5. Creating an image post.
6. Creating a video post.
7. Commenting on published posts.
8. Deleting comments.
9. Reading all published posts of a given user.
10. Reading all published comments of a given user.
11. Reading all published posts available on the site arranged chronologically.

<br><br>

- **Create Image Post**
![Create Image Post](/static/assets/img/create-image-post.png)

<br><br>

- **Create Post View (General)**
![Create Post View](/static/assets/img/create-post-view.png)

<br><br>

- **Create Text Post**

![Create Text Post](/static/assets/img/create-text-post.png)

<br><br>

- **Create Video Post**

![Create Video Post](/static/assets/img/create-video-post.png)

<br><br>

- **Delete Post Button**

![Delete Post](/static/assets/img/delete-post-button.png)

<br><br>

- **Delete Profile**

![Delete Profile](/static/assets/img/delete-profile-view.png)

<br><br>

- **Edit Profile**

![Edit Profile One](/static/assets/img/edit-profile-view.png)

![Edit Profile Two](/static/assets/img/edit-profile-two.png)

<br><br>

- **View User Comments/Delete Comment**

![View and Delete Comments](/static/assets/img/view-own-comments-logged-in.png)

<br><br>

- **View User Posts**

![View User Posts](/static/assets/img/view-user-posts.png)

<br><br>

- **Sign Up/Register an Account**

![Sign Up/Register](/static/assets/img/signup.png)

## Agile Development for PianoPhiles

PianoPhiles was developed using an Agile-inspired approach, emphasizing iterative development and incremental improvements. Here's how the project progressed through sprints and milestones:

#### Sprint 1: Project Initiation

- Project Setup:
  - Create basic ERD, site flow logic diagram and wireframes as basis for project.
  - Create the Django project, app and superuser.
  - Install essential packages like Django, dj_database_url, psycopg2, and cloudinary-storage.
  - Update project files, including settings.py, env.py, and the Procfile for deployment.
  - Initiate database setup and perform migrations.
  - Develop a base.html for the site's layout.


#### Sprint 2: Basic Model and View Development

- Main Model Development:
  - Set up database models and decide necessary attributes required for Post, TexPost, VideoPost, ImagePost and PostComment     
    models.
  - Add basic sign up, sign in, sign out pages using allauth packaged.
  - Integrated crispy-forms and crispy-bootstrap5 for form rendering.
  - Create Profile model.
  - Link data from allauth forms to Profile model.
  - Create basic views and url paths to check that models are actually rendering.
  - Created a README with an initial project layout.

#### Sprint 3: Customise Views and Content 

- Enhancements and Features:
  - Add more specific CSS stylings in addition to Bootstrap to customise views.
  - Implement forms and views for uploading post (image, text, video) to database.
  - Add forms and views for updating and deleting profile.
  - Develop supplementary views such as user comments and user posts views.
  - Add Masonry to better style post list view.

#### Sprint 4: Refining CSS and Adding Functionality

- CSS and Styling:
  - Enhance CSS styles for the banner.
  - Refine the styling of the post previews in post list view and add floating style to "add post" button.

- Additional Features:
  - Add filtering differentiating which information is available to authenticated and non-authenticated users.
  - Add status messages so users know their comments are pending approval.
  - Set up automated tests.

#### Sprint 5: Testing, Revisions, and Documentation 

- Testing and Quality Assurance:
  - Conducted thorough testing, including HTML, CSS, and Python testing.
  - Utilise the coverage package to generate a coverage report.
  - Address HTML and CSS testing errors and warnings.
  - Remove commented-out code and perform code cleanup.

- Documentation and Finalization:
  - Compile test results and include images in the README.md file.
  - Enrich the README with detailed information about features.
  - Ensure DEBUG is set to False before deployment.
  - Conduct final code and documentation proofreading.

- Deployment:
  - Finalise the README.
  - Prepare the project for the final deployment.

In order to keep track of progress through these sprints, I used [Notion's](www.notion.so) Kanban capabilities. Being a Notion user already, the interface is comfortable and intuitive to me.

As you can see from the following screenshots, I grouped tasks defined by user stories according to epics.


<details>
<summary>General View of Epics in Notion Kanban</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_1.png">
</details>

<details>
<summary>Further General View of Epics in Notion Kanban</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_2.png">
</details>

<details>
<summary>Further General View of Epics in Notion Kanban</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_3.png">
</details>

<details>
<summary>View of Tasks in Content and Navigation Epic</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_4.png">
</details>

<details>
<summary>View of Tasks in Registration and User Information Epic</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_5.png">
</details>

<details>
<summary>View of Tasks in Managing Posts and Comments Epic</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_6.png">
</details>

<details>
<summary>View of Tasks in User Views Epic</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_7.png">
</details>

<details>
<summary>View of Tasks in Styling Epic</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_8.png">
</details>

<details>
<summary>View of Tasks and Future Features to be Added in Future Development of PianoPhiles</summary>
<img src="/static/assets/img/notion_pianophiles_kanban_9.png">
</details>





By following this Agile-inspired approach with well-defined sprints, PianoPhiles was able to evolve incrementally, ensuring a user-friendly and feature-rich platform for piano enthusiasts. Continuous testing, feedback, and iterative development contributed to the project's success.

## Testing and Validation

### Performance

- **Lighthouse Report**

Google Lighthouse was used to test the performance of this site. Overall performance is affected by the dominance of large images and video files on the site, however it is still relatively strong. 

While the score of 83 suggests room for further improvement in best practices, most of the logged issues tend to be related to serving the images from Cloudinary, something that is unlikely to change currently given the scope and purpose of this project.

SEO and Accessability scores were favourable.

![Lighthouse Report](/static/assets/img/lighthouse-report-pianophiles.png)

- **WAVE Report**

The web accessibility evaluation tool WAVE by WebAIM was used to ensure the site meets high accessibility standards.

![Wave Report](/static/assets/img/wave-report.png)


- **HTML Validation**

W3C's HTML validator was used to validate the HTML for all of the site pages.

<details>
<summary>Home Page</summary>
<img src="/static/assets/img/homepage-html-test.png">
</details>
<details>
<summary>Create Post Page</summary>
<img src="/static/assets/img/create-post-html-test.png">
</details>
<details>
<summary>Create Text Post Page</summary>
<img src="/static/assets/img/create-text-post-html-test.png">
</details>
<details>
<summary>Create Image Post Page</summary>
<img src="/static/assets/img/create-image-post-test.png">
</details>
<details>
<summary>Create Video Post Page</summary>
<img src="/static/assets/img/create-video-post-test.png">
</details>
<details>
<summary>Delete Profile Page</summary>
<img src="/static/assets/img/delete-profile-test.png">
</details>
<details>
<summary>Edit Profile Page</summary>
<img src="/static/assets/img/edit-profile-html-test.png">
</details>
<details>
<summary>Login Page</summary>
<img src="/static/assets/img/login-html-test.png">
</details>
<details>
<summary>Logout Page</summary>
<img src="/static/assets/img/logout-html-test.png">
</details>
<details>
<summary>Post Detail Page</summary>
<img src="/static/assets/img/post-detail-test.png">
</details>
<details>
<summary>Profile Page</summary>
<img src="/static/assets/img/profile-html-test.png">
</details>
<details>
<summary>Signup Page</summary>
<img src="/static/assets/img/signup-test.png">
</details>
<details>
<summary>User Comments Page</summary>
<img src="/static/assets/img/user-comments-html-test.png">
</details>
<details>
<summary>User Posts Page</summary>
<img src="/static/assets/img/user-posts-html-test.png">
</details>


- **CSS Validation**

W3C's CSS validator was used to validate the CSS for this site.

<details>
<summary>CSS Validation</summary>
<img src="/static/assets/img/css-validation.png">
</details>

- **JSHint**

JSHint was used to validate the very few pieces of JavaScript in this project.

<details>
<summary>Floating Button JS Script</summary>
<img src="/static/assets/img/floating-button-validation.png">
</details>


<details>
<summary>Masonry Styling JS Script</summary>
<img src="/static/assets/img/masonry-js-validation.png">
</details>


<details>
<summary>Create Post JS Script</summary>
<img src="/static/assets/img/create-post-js-validation.png">
</details>


- **Python Validation**

Code Institute's Python Linter was used to validate the Python code in this project. While there are some lines that are deemed "too long", the linter did not detect any other kinds of errors.

<details>
<summary>admin.py</summary>
<img src="/static/assets/img/admin.py-test.png">
</details>

<details>
<summary>apps.py</summary>
<img src="/static/assets/img/app.py-test.png">
</details>

<details>
<summary>forms.py</summary>
<img src="/static/assets/img/forms.py-test.png">
</details>

<details>
<summary>models.py</summary>
<img src="/static/assets/img/models.py-test.png">
</details>

<details>
<summary>views.py</summary>
<img src="/static/assets/img/views.py-test.png">
</details>

<details>
<summary>urls.py</summary>
<img src="/static/assets/img/urls.py-test.png">
</details>

<details>
<summary>urls.py (project level)</summary>
<img src="/static/assets/img/urls.py-project-test.png">
</details>

<details>
<summary>settings.py</summary>
<img src="/static/assets/img/settings.py-test.png">
</details>

<details>
<summary>views.py (project level)</summary>
<img src="/static/assets/img/views.py-project-level.png">
</details>

<details>
<summary>models_tests.py</summary>
<img src="/static/assets/img/models_tests_validation.png">
</details>

<details>
<summary>forms_tests.py</summary>
<img src="/static/assets/img/forms_tests_validation.png">
</details>

<details>
<summary>views_tests.py</summary>
<img src="/static/assets/img/views_tests_validation.png">
</details>


### Manual Testing

**EPIC: CONTENT AND NAVIGATION**
| ID | User Story | Action/Expected Results | Pass/Fail |
| -- | ---------- | ----------------------- | ---- |
| 1A | 	As a user, I want to be able to easily navigate through the content available on the site. | A nav bar with links to the main pages of the site is always available to any user using the site, whether logged in or not. When the screen size becomes smaller, the nav links collapse into a hamburger menu. | Pass |
| 1B | As a user, I want to see relevant information about the site and its content easily so I can decide if I want to register an account. | Any user who accesses the site will see the PianoPhiles logo and tag line "For piano freaks and geeks". While this doesn't explicitly say "this is a blog post website for piano enthusiasts", I do think this in combination with the immediately visible list of posts on the homepage make the site's purpose obvious. | Pass |
| 1C | As a user, I want the design of the site to be simple, intuitive and appealing. | The minimal styling of the site combined with the masonry effect used make the information on the site easy to delineate and interpret. | Pass |
| 1D | As a user, I want to be able to access different areas of the site e.g. detailed blog posts, or user profiles with ease so that I may easily enjoy the feautures the site has to offer. | Any user can access the site's most basic functions from the nav bar. Any user can easily access profiles by clicking on user profile photos in the post list view. Posts are easily explored by clicking the preview. | Pass |

**EPIC: REGISTRATION AND USER INFORMATION**
| ID | User Story | Action/Expected Results | Pass/Fail |
| -- | ---------- | ----------------------- | ---- |
| 2A | As a user, I want to create my own profile, so I have a familiar and comfortable place where I can share my enthusiasm for piano and keep track of discussions, as well as accessing all the functionality the site has to offer.| An unregistered user will see a 'Register' link in the navig bar upon accessing the site, and this will always be available as long as they are not logged in. Clicking on this brings the user to the account registration page. | Pass |
| 2B | As a user, I want to be able to edit my profile so that it reflects me as I change. | An "Edit Profile" is available to all logged in users when they visit their own profile. This allows them to update their bio section and profile photo.  | Pass |
| 2C | As a user, I want to be able to log into my account easily, so I can access my account information. | Any user not logged into the site can do so by clicking the "Login" link in the nav bar. | Pass |
| 2D | As a user, I want to be able to log out of my account with ease to protect my account information. | Any logged in user can log out by pressing the "Logout" button in the nav bar. | Pass |
| 2E | As a user, I want to be able to delete my account information/profile if I feel the site community no longer reflects my values. | Any user with an account is free to delete it any time by pressing the "Delete Profile" button available from their profile page. | Pass |
| 2F | As a user, I also want the option of being able to use the site passively without registering an account, even if this means I can't access some site functionality like making posts or comments. | Account registration is not required to read the published content on the site. | Pass |

**EPIC: MANAGING POST AND COMMENTS**
| ID | User Story | Action/Expected Results | Pass/Fail |
| -- | ---------- | ----------------------- | ---- |
| 3A | As an authenticated user, I want to be able to create text posts so that I can share my enthusiasm with my online community. | All authenticated logged in users can create posts by clicking on the red and white 'plus' button at the bottom right hand corner of every page. | Pass |
| 3B | As an authenticated user, I want to be able to create image posts so that I can share my enthusiasm with my online community. | After clicking the 'add a post'/'plus' button, all authenticated logged in users will be brought to the general "create post" page where they have the option of opening a form specifically for creating image posts. It allows them to upload image files given a specified file size and format as well as title information. The image file is hosted from Cloudinary. | Pass |
| 3C | As an authenticated user, I want to be able to create video posts so that I can share my enthusiasm with my online community. | After clicking the 'add a post'/'plus' button, all authenticated logged in users will be brought to the general "create post" page where they have the option of opening a form specifically for creating video posts. It allows them to upload video files given a specified file size and format as well as title information. The video file is hosted from Cloudinary. | Pass |
| 3D | 	As an authenticated user, I want to be able to delete my posts if I feel they no longer reflect my opinions. | A "Delete Post" button is available to all logged in authenticated users when viewing their posts from the PostList or Profile views. | Pass |
| 3E | 	As an authenticated user, I want to be able to comment on other users' posts in order to encourage discussion and a sense of community. | All logged in authenticated users are able to comment on published posts by entering their comments into the comment form from the PostDetail view. | Pass |
| 3F | 	As an authenticated user, I want to be able to delete my past comments if I feel they no longer reflect my opinions.| All logged in authenticated users are able to delete their comments by pressing the "Delete Comment" button that is available on all of their own comments when using the Profile view or UserComments view. | Pass |
| 3G | 	As an authenticated user, I want to be able to delete my past comments if I feel they no longer reflect my opinions.| All logged in authenticated users are able to delete their comments by pressing the "Delete Comment" button that is available on all of their own comments when using the Profile view or UserComments view. | Pass |

**EPIC: USER VIEWS**
| ID | User Story | Action/Expected Results | Pass/Fail |
| -- | ---------- | ----------------------- | ---- |
| 4A | 	As a user, I want to be able to see all publicly available posts so that I can browse through them. | All users can view all published posts arranged in chronological order on the homepage. This page is paginated to prevent the browser from having to load too much data all at the same time when loading the site. | Pass |
| 4B | As a user, I want to be able to view the detail of all publicly available posts, so I can read the full content associated with them, including comments. | All users can access full posts details by clicking on their previews from the PostList (homepage) view. | Pass |
| 4C | As a user, I want to be able to view the record of a given user's publicly available posts and comments. | Any user can view all of the published posts associated with a given user by visiting their profile. They can access their most recenty published comments too, but only a logged in authenticated user can access the full list of published comments. | Pass |
| 4D | As an authenticated user, I want to be able to view a record of all my publicly available posts. | All authenticated logged in users can view a list of all their published posts by visiting their profile and pressing the "View All Posts" button. | Pass |
| 4E | As an authenticated user, I want to be able to view a record of all my publicly available comments. | All logged in authenticated users can view a list of all their published comments by clicking the "View All Comments" button on their profile. | Pass |

### Automated Testing

Automated tests were written using help from Code Institute's instructional videos as part of their "Hello Django" walkthrough project. Different aspects of the models, forms and views were tested. Due to time constraints, further learning required and given that automated testing was not required as part of the rubric for this project, these tests are not fully comprehensive but were written to demonstrate a basic understanding of automated tests.

I also took guidance from reading previous questions in Code Institute's Slack Channel, Ulrike Riemenschneider's project, [World Travel Log](https://github.com/URiem/worldtravellog) and [Mozilla's documentation on Django testing.](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)

#### Views Tests (views_tests.py)
<br><br>

![Screenshot to show successful running of views_tests.py](/static/assets/img/views_tests_screenshot.png)
<br><br>

#### Views Tests (forms_tests.py)
<br><br>

![Screenshot to show successful running of forms_tests.py](/static/assets/img/forms_test_screenshot.png)
<br><br>

#### Views Tests (models_tests.py)
<br><br>

![Screenshot to show successful running of models_tests.py](/static/assets/img/models_tests_screenshot.png)

<br><br>

#### Coverage Report

This coverage report was generated using the coverage package. As you can see there is room for further exploration in automated testing to achieve greater coverage.
<br><br>

![Coverage Report](/static/assets/img/coverage_report_screenshot.png)



## Deployment

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

## Deploying the Project by Forking and Cloning

1. **Fork the Repository**:
   - Go to your Django project's GitHub repository.
   - Click the "Fork" button in the upper right corner of the repository page. This will create a copy of the repository under your GitHub account.

2. **Clone the Forked Repository**:
   - Open your terminal or command prompt.
   - Change your working directory to where you want to store the project:
     ```bash
     cd /path/to/your/local/folder
     ```
   - Clone the forked repository to your local machine. Replace `<your_username>` with your GitHub username and `<repository_name>` with the name of your repository:
     ```bash
     git clone https://github.com/<your_username>/<repository_name>.git
     ```

3. **Navigate to the Project Directory**:
   - Change your working directory to the project's directory:
     ```bash
     cd <repository_name>
     ```

4. **Install Dependencies**:
   - Create a virtual environment for your project (if you haven't already) and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install the project's dependencies from the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

5. **Configure Environment Variables**:
   - Create a `.env` file in your project directory and set the necessary environment variables, such as `SECRET_KEY`, `DATABASE_URL`, and any others required by your Django project.

6. **Run Migrations**:
   - Apply database migrations to create the database schema:
     ```bash
     python manage.py migrate
     ```

7. **Start the Development Server**:
   - Run the Django development server to test your project locally:
     ```bash
     python manage.py runserver
     ```
   - Your Django app should now be running locally. Open your web browser and access it at `http://localhost:8000`.

8. **Test the App Locally**:
   - Interact with your app to ensure it's functioning correctly in the local development environment.

9. **Development and Testing**:
   - Make any necessary changes and test your app locally to ensure it works as expected.

10. **Push Changes to GitHub**:
    - Once you are satisfied with your changes, commit them locally and push them to your forked GitHub repository:
      ```bash
      git add .
      git commit -m "Add local development changes"
      git push origin master
      ```

Now, you have successfully deployed your Django project locally by forking the repository, cloning it, and running it on your machine. You can continue to develop and test your project locally before deploying it to Heroku using the steps mentioned in the earlier section.



## Technologies Used

 - Languages Used:
    - HTML
    - CSS
    - JS
    - Python

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

- [coverage](https://pypi.org/project/coverage/) - Version 7.3.1
  - A tool for measuring code coverage of Python programs. Useful for ensuring that your tests are thorough.

- [pytest](https://docs.pytest.org/en/latest/) - Version 7.4.2
  - A popular testing framework for Python that makes it easy to write simple and scalable test cases for your code.


### Bugs and Future Features

 - Immediate Issues: 
    - There are remaining issues in the application to be addressed. For example, the floating modal that appears when hovering over the "add post" button appears too far away from the actual button. Design throughout the site is quite general and relies too much on Bootstrap's default styles. The 'like' button acts as a redirect rather than a dynamic toggling switch which does not make for good UX. It is also only available from the PostList view. The use of space in forms could be more balanced and made more attractive. Different font sizes used do not always highlight the hierarchy of content with great specificity. The profile picture icons sometimes distort the profile images slightly. The colouring of the comments section in PostDetail views is not particularly attractive.
    There are even more issues that could be listed but these would be a good place to begin with for immediate future development.

- Future Features:
  As I continue to develop the project over the coming months I would like to implement:
  - Search function allowing users to search by keyword for particular posts or posts relating to a specific subject.
  - Tag function allowing posts to be categorised with hastags.
  - Reply function allowing users to reply to specific comments as opposed to all comments being listed only in a chronlogical chain.
  - Private messaging feature allowing users to correspond with others directly.
  - Site categorisation. This is a more large scale general goal. I imagine the site having three separate wings where users can investigate content relating to classical piano, jazz piano or contemporary/pop piano in their own dedicated spaces.


### Acknowledgements

Several of the Class based models and their associated functions were taken directly from or modeled on the code used in Code Institute's Codestar Blog project.

Tips on pagination came from this website: https://realpython.com/django-pagination/#using-the-django-paginator-in-views

Advice on having issues with getting Cloudinary to serve static files correctly to Heroku were taken from several Stack Overflow posts - https://stackoverflow.com/questions/72837010/cannot-push-to-heroku-with-cloudinary-storing-my-staticfiles

https://stackoverflow.com/questions/70231804/how-can-i-upload-all-types-of-files-videos-audios-pdfs-zip-in-cloudinary-in

YouTube tutorials on Cloudinary and Django: https://www.youtube.com/watch?v=fQo9ivqX4xs
https://www.youtube.com/watch?v=i0ar7W98Osc

Article on editing the Summernote editor: https://djangocentral.com/integrating-summernote-in-django/

In addition to guidance from Code Institute's "Hello Django" walkthrough project, further advice on implementing automated testing was taken from [Mozilla's documentation on Django testing.](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing).

The layout of this README document is heavily influenced by Ulrike Riemenschneider's project, [World Travel Log](https://github.com/URiem/worldtravellog). 





















  

