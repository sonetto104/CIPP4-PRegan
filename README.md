
# PianoPhiles

PianoPhiles is a blog site for piano lovers where they can share clips of their favourite performances, post questions about technique or interpretation, or share pictures of their fun piano moments. As well as being able to share content in text, image and video format, users can discuss the material with other likeminded keyboard enthusiasts through comments, show their appreciation with likes and add a personal touch to their own profile page with a short bio and profile photo. Let's get tinkling those keys!



- User Stories
  1. As a user I want to create my own profile, so I have a familiar and comfortable place where I can share my enthusiasm for piano and keep track of discussions.
  2. As a user I want to be able to view all the most recent posts on the site so I can keep my interest fresh and novel.
  3. As a user I want to be able to view all my past posts so I can keep track of my public correspondences.
  4. As a user I want to be able to view all past posts of other users so I can develop understanding and see how other people's opinions develop too.
  5.  As a user I want to be able to comment on posts to allow for interaction and community.
  6.  As a user I want to be able to view all my past comments so I have a written record of my interactions.
  7.  As a user I want to be able to view the comments of other users so I can see how opinions and understanding develop and change.
  8.  As a user I want to be able to edit my profile so that it reflects me as I change.
  9.  As a user I want to be able to delete previous posts I made if I feel they no longer reflect my opinions
  10. As a user I want to be able to delete previous comments I made if I feel they no longer reflect my opinions.
  11. As a user I want to be able to like posts to show appreciation.
  12. As a user I want to be able to delete my profile if I don't feel the community reflects my values any more.
  13. As a user I want to be able to view the site without having to sign up for a profile if I think I would enjoy a more passive rolw on the site.
  14. As a user I want to be able to log in or out of my profile if I feel like "laying low". 

- Site Goal

  - The goal of the site is to create a place where piano lovers can really sink their teeth into their favourite arguments about the art. Spaces like pianostreet used to thrive in the early days of popular widespread internet, but due to their lack of design and ui development, that community has fizzled out and is nowhere near as active as it used to be. It would be nice to resurrect that fun community online where people had ridiculous arguments about interpreting Chopin.

- Target Audience

  -Users of the site are likely to be advanced second level and conservatoire level student pianists and retired amateur pianists; a reflection of the real life piano recital going audience.


- Is the content relevant?

This content is ultimately frivolous, but there I do believe there is a genuine desire for discussion among musicians, and in the Instagram age, what's not to enjoy about the press campaigns of our favourite stars?

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

    - Profile functionality where users can choose whether or not to share information about themselves, and where they can access their history of activity,     
    notifications etc.
- Ability to like posts.
- Dynamic like button.

- Could Have
    - Live chat feature.
    - Different genres for classical, jazz and pop.
    - Search functionality.
    - Tag functionality so users can search by tags, keywords or genre.

### Structure Plane


### Skeleton Plane

As per the requirements of Code Institute's Portfolio Project 4 assignment, this functions at the most basic level as a CRUD application.

C - Users can create profiles, comments and posts.
R - Users can read the profiles, comments and posts of other users. They can read their own comments and posts.
U - Users can edit their profiles.
D - Users can delete their past comments, posts and their profile.

#### Site Flow

Most of the site should flow centrally from the home page. I used Lucid Chart to make a diagram with a rough outline of how the site should flow.

![Site Flow Diagram](static/assets/img/pianophiles-siteflow.jpg)


#### Database Schema

The project utilizes PostgreSQL as the database technology of choice. This is evident from the inclusion of the psycopg2 package in the requirements file, which serves as the PostgreSQL adapter for Python. PostgreSQL is a powerful and feature-rich open-source relational database management system known for its reliability, scalability, and extensive support for advanced data types and SQL features. Additionally, the project leverages the dj-database-url package, which facilitates the handling and parsing of database URLs. This allows for seamless configuration of the database connection using a URL format specified by the PostgreSQL provider. By utilizing these database technologies, the project ensures efficient and secure data storage and retrieval, enabling robust and scalable web application functionality.

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



#### Wireframes

I used Figma to make these basic wireframes for how I imagined the website would look.

![Sample Profile Layout](static/assets/img/android-small.jpg)

![Sample Login Page Layout](static/assets/img/android-small-page-1.jpg)

![Sample Post Page Layou](static/assets/img/android-small-page-2.jpg)




















  - Django docs
  - Bootstrap Docs
  - W3Schools

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
