ai_output_roadmap = """
{
  "topic": "Web Development",
  "total_duration": "17 weeks",
  "steps": [
    {
      "step_number": 1,
      "title": "Frontend Styling with CSS",
      "technology": "CSS",
      "duration": 2,
      "perquisites": ["html"],
      "difficulty_level": 2.0,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 95,
      "study_hours_per_day": 7200,
      "description": "Learn to style web pages using Cascading Style Sheets (CSS) to control layout, colors, fonts, and responsiveness, enhancing the visual presentation of HTML content.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "MDN Web Docs: CSS Basics",
          "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp: Responsive Web Design Certification (CSS section)",
          "url": "https://www.freecodecamp.org/learn/responsive-web-design/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "The Complete Guide to CSS",
          "url": "https://www.udemy.com/course/css-the-complete-guide-incl-flexbox-grid-sass/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Advanced CSS and Sass: Flexbox, Grid, Animations and More!",
          "url": "https://www.udemy.com/course/advanced-css-and-sass/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 2,
      "title": "Frontend Interactivity with JavaScript Fundamentals",
      "technology": "JavaScript",
      "duration": 3,
      "perquisites": ["html", "CSS"],
      "difficulty_level": 2.5,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 90,
      "study_hours_per_day": 7200,
      "description": "Master the fundamentals of JavaScript to add dynamic and interactive behavior to web pages, including DOM manipulation, event handling, and basic programming constructs.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "MDN Web Docs: JavaScript Guide",
          "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp: JavaScript Algorithms and Data Structures",
          "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "The Complete JavaScript Course 2024: From Zero to Expert!",
          "url": "https://www.udemy.com/course/the-complete-javascript-course-2024-from-zero-to-expert/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "JavaScript: Understanding the Weird Parts",
          "url": "https://www.udemy.com/course/understand-javascript/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 3,
      "title": "Version Control with Git & GitHub",
      "technology": "Git",
      "duration": 1,
      "perquisites": [],
      "difficulty_level": 2.0,
      "depth": 2,
      "topic": "Development Tools",
      "is_category": false,
      "importance_score": 85,
      "study_hours_per_day": 7200,
      "description": "Learn to use Git for version control to track changes in code, collaborate with others, and manage project history effectively using platforms like GitHub.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Pro Git Book",
          "url": "https://git-scm.com/book/en/v2",
          "type": "documentation"
        },
        {
          "name": "GitHub Docs: Getting Started",
          "url": "https://docs.github.com/en/get-started",
          "type": "documentation"
        }
      ],
      "paid_resources": [
        {
          "name": "Git Complete: The definitive, step-by-step guide to Git",
          "url": "https://www.udemy.com/course/git-complete/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Git & GitHub - The Practical Guide",
          "url": "https://www.udemy.com/course/git-and-github-bootcamp/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 4,
      "title": "Introduction to a Frontend Framework (React)",
      "technology": "React",
      "duration": 3,
      "perquisites": ["html", "CSS", "JavaScript"],
      "difficulty_level": 3.0,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 80,
      "study_hours_per_day": 7200,
      "description": "Understand the core concepts of React to build modern, component-based user interfaces, including JSX, state management, props, and component lifecycle.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "React Official Documentation: Main Concepts",
          "url": "https://react.dev/learn",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp: Front End Development Libraries (React section)",
          "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "React - The Complete Guide (incl Hooks, React Router, Redux)",
          "url": "https://www.udemy.com/course/react-the-complete-guide-incl-redux/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Modern React with Redux",
          "url": "https://www.udemy.com/course/react-redux/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 5,
      "title": "Backend Development with Flask (Python)",
      "technology": "Flask",
      "duration": 3,
      "perquisites": ["Python", "html"],
      "difficulty_level": 3.0,
      "depth": 2,
      "topic": "Backend",
      "is_category": false,
      "importance_score": 75,
      "study_hours_per_day": 7200,
      "description": "Utilize Python with the Flask microframework to build server-side logic, handle HTTP requests, manage routes, and render dynamic web pages.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Flask Official Documentation: Quickstart",
          "url": "https://flask.palletsprojects.com/en/latest/quickstart/",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp: Learn Flask for Python - Full Tutorial",
          "url": "https://www.freecodecamp.org/news/learn-flask-for-python-full-tutorial/",
          "type": "tutorial"
        }
      ],
      "paid_resources": [
        {
          "name": "Python and Flask Bootcamp: Create Websites using Flask!",
          "url": "https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "The Flask Mega-Tutorial (by Miguel Grinberg)",
          "url": "https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world",
          "type": "course",
          "platform": "Personal Blog/Book"
        }
      ]
    },
    {
      "step_number": 6,
      "title": "Database Fundamentals (SQL & SQLAlchemy)",
      "technology": "SQL",
      "duration": 2,
      "perquisites": ["Python", "Flask"],
      "difficulty_level": 3.5,
      "depth": 2,
      "topic": "Database",
      "is_category": false,
      "importance_score": 70,
      "study_hours_per_day": 7200,
      "description": "Learn to design, query, and manage relational databases using SQL, and integrate them with Python applications using an ORM like SQLAlchemy.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "SQLZoo: Interactive SQL Tutorials",
          "url": "https://sqlzoo.net/",
          "type": "tutorial"
        },
        {
          "name": "W3Schools: SQL Tutorial",
          "url": "https://www.w3schools.com/sql/",
          "type": "tutorial"
        }
      ],
      "paid_resources": [
        {
          "name": "The Complete SQL Bootcamp 2024: Go from Zero to Hero",
          "url": "https://www.udemy.com/course/the-complete-sql-bootcamp/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Python and PostgreSQL: Build a REST API with Flask",
          "url": "https://www.udemy.com/course/python-and-postgresql-build-a-rest-api-with-flask/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 7,
      "title": "RESTful API Development & Integration",
      "technology": "REST API",
      "duration": 2,
      "perquisites": ["Flask", "SQL", "React"],
      "difficulty_level": 4.0,
      "depth": 2,
      "topic": "Backend",
      "is_category": false,
      "importance_score": 65,
      "study_hours_per_day": 7200,
      "description": "Design and implement RESTful APIs using Flask to enable communication between the frontend (React) and backend, handling data exchange and CRUD operations.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "MDN Web Docs: An introduction to APIs",
          "url": "https://developer.mozilla.org/en-US/docs/Web/API",
          "type": "documentation"
        },
        {
          "name": "Postman Learning Center: API Basics",
          "url": "https://learning.postman.com/docs/introduction/overview/",
          "type": "documentation"
        }
      ],
      "paid_resources": [
        {
          "name": "Build a REST API with Python & Flask",
          "url": "https://www.udemy.com/course/rest-api-flask-and-python/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "REST APIs with Flask and Python",
          "url": "https://www.coursera.org/projects/rest-apis-with-flask-and-python",
          "type": "course",
          "platform": "Coursera"
        }
      ]
    },
    {
      "step_number": 8,
      "title": "Deployment Basics",
      "technology": "Heroku",
      "duration": 1,
      "perquisites": ["Flask", "React", "Git"],
      "difficulty_level": 3.0,
      "depth": 2,
      "topic": "DevOps",
      "is_category": false,
      "importance_score": 60,
      "study_hours_per_day": 7200,
      "description": "Learn to deploy full-stack web applications to cloud platforms like Heroku, understanding concepts of hosting, environment variables, and continuous deployment.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Heroku Dev Center: Getting Started with Python",
          "url": "https://devcenter.heroku.com/articles/getting-started-with-python",
          "type": "documentation"
        },
        {
          "name": "Heroku Dev Center: Getting Started with React",
          "url": "https://devcenter.heroku.com/articles/create-react-app-buildpack",
          "type": "documentation"
        }
      ],
      "paid_resources": [
        {
          "name": "Deploying a Full Stack Application to Heroku",
          "url": "https://www.udemy.com/course/deploying-a-full-stack-application-to-heroku/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "The Ultimate Guide to Deploying Web Applications",
          "url": "https://www.udemy.com/course/the-ultimate-guide-to-deploying-web-applications/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    }
  ]
}
"""
