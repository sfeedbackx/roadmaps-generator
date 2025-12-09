ai_output_roadmap = """
{
  "topic": "Web Development",
  "total_duration": "15 weeks",
  "steps": [
    {
      "step_number": 1,
      "title": "CSS Fundamentals & Responsive Design",
      "technology": "CSS",
      "duration": 2,
      "perquisites": ["HTML"],
      "difficulty_level": 2.0,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 85,
      "study_hours_per_day": 10800,
      "description": "Styling web pages with CSS, including selectors, properties, and values. Implementing responsive design principles using media queries, Flexbox, and CSS Grid to ensure websites adapt to various screen sizes.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "MDN Web Docs: CSS Basics",
          "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp Responsive Web Design Certification",
          "url": "https://www.freecodecamp.org/learn/responsive-web-design/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "Responsive Web Design with CSS: A Complete CSS Guide",
          "url": "https://www.udemy.com/course/responsive-web-design-with-css-a-complete-css-guide/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Build Responsive Real-World Websites with HTML and CSS",
          "url": "https://www.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 2,
      "title": "JavaScript Basics & DOM Manipulation",
      "technology": "JavaScript",
      "duration": 2,
      "perquisites": ["HTML", "CSS"],
      "difficulty_level": 2.5,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 90,
      "study_hours_per_day": 10800,
      "description": "Adding interactivity to web pages using JavaScript, covering variables, data types, functions, control flow, and manipulating the Document Object Model (DOM) to dynamically change content and styles.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "MDN Web Docs: JavaScript Guide",
          "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp JavaScript Algorithms and Data Structures",
          "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "The Complete JavaScript Course 2024: From Zero to Expert!",
          "url": "https://www.udemy.com/course/the-complete-javascript-course/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Programming Foundations with JavaScript, HTML and CSS",
          "url": "https://www.coursera.org/learn/programming-foundations-with-javascript-html-css",
          "type": "course",
          "platform": "Coursera"
        }
      ]
    },
    {
      "step_number": 3,
      "title": "Python Web Framework - Flask Introduction",
      "technology": "Flask",
      "duration": 2,
      "perquisites": ["Python", "HTML"],
      "difficulty_level": 3.0,
      "depth": 2,
      "topic": "Backend",
      "is_category": false,
      "importance_score": 88,
      "study_hours_per_day": 10800,
      "description": "Building simple web applications and understanding server-side logic using the Flask microframework. This includes routing, templates (Jinja2), and handling HTTP requests.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Flask Official Documentation",
          "url": "https://flask.palletsprojects.com/en/latest/tutorial/",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp Python for Everybody (covers Python basics, useful for Flask context)",
          "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/",
          "type": "course"
        }
      ],
      "paid_resources": [
        {
          "name": "Web Developer Bootcamp with Flask and Python in 2024",
          "url": "https://www.udemy.com/course/the-complete-python-flask-course/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Python and Flask Framework Complete Course",
          "url": "https://www.udemy.com/course/python-and-flask-framework-complete-course/",
          "type": "course",
          "platform": "Udemy"
        }
      ]
    },
    {
      "step_number": 4,
      "title": "Database Fundamentals - SQL & ORMs",
      "technology": "SQL, SQLAlchemy",
      "duration": 2,
      "perquisites": ["Python", "Flask Basics"],
      "difficulty_level": 3.0,
      "depth": 2,
      "topic": "Database",
      "is_category": false,
      "importance_score": 92,
      "study_hours_per_day": 10800,
      "description": "Understanding relational databases, writing SQL queries for data manipulation (CRUD operations), and integrating databases with Flask applications using an Object-Relational Mapper (ORM) like SQLAlchemy.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "SQLZoo Interactive SQL Tutorial",
          "url": "https://sqlzoo.net/",
          "type": "tutorial"
        },
        {
          "name": "SQLAlchemy Documentation",
          "url": "https://docs.sqlalchemy.org/en/latest/orm/tutorial.html",
          "type": "documentation"
        }
      ],
      "paid_resources": [
        {
          "name": "SQL for Data Analytics",
          "url": "https://www.udemy.com/course/sql-for-data-analytics-a-complete-guide/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Databases and SQL for Data Science with Python",
          "url": "https://www.coursera.org/learn/databases-and-sql-for-data-science-with-python",
          "type": "course",
          "platform": "Coursera"
        }
      ]
    },
    {
      "step_number": 5,
      "title": "Building RESTful APIs with Flask",
      "technology": "Flask-RESTful",
      "duration": 2,
      "perquisites": ["Flask Basics", "SQL & ORMs"],
      "difficulty_level": 3.5,
      "depth": 2,
      "topic": "Backend",
      "is_category": false,
      "importance_score": 95,
      "study_hours_per_day": 10800,
      "description": "Designing and implementing RESTful API endpoints using Flask, handling JSON data, and managing HTTP methods (GET, POST, PUT, DELETE) for client-server communication.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Flask-RESTful Documentation",
          "url": "https://flask-restful.readthedocs.io/en/latest/",
          "type": "documentation"
        },
        {
          "name": "Build a REST API using Flask - Python (GeeksforGeeks)",
          "url": "https://www.geeksforgeeks.org/build-a-rest-api-using-flask-python/",
          "type": "tutorial"
        }
      ],
      "paid_resources": [
        {
          "name": "Build REST APIs with Flask and Python (The Complete Course)",
          "url": "https://www.udemy.com/course/rest-api-flask-and-python/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 1",
          "url": "https://realpython.com/flask-connexion-rest-api/",
          "type": "tutorial",
          "platform": "Real Python"
        }
      ]
    },
    {
      "step_number": 6,
      "title": "Frontend Framework - React.js Basics",
      "technology": "React.js",
      "duration": 3,
      "perquisites": ["JavaScript Basics", "HTML", "CSS"],
      "difficulty_level": 3.5,
      "depth": 2,
      "topic": "Frontend",
      "is_category": false,
      "importance_score": 90,
      "study_hours_per_day": 10800,
      "description": "Learning the fundamentals of React.js, including components, JSX, props, state, and basic hooks to build dynamic and reactive user interfaces.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "React Official Documentation - Main Concepts",
          "url": "https://react.dev/learn",
          "type": "documentation"
        },
        {
          "name": "freeCodeCamp Front End Development Libraries (React section)",
          "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/#react",
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
          "name": "Frontend Development with React",
          "url": "https://www.coursera.org/learn/front-end-react",
          "type": "course",
          "platform": "Coursera"
        }
      ]
    },
    {
      "step_number": 7,
      "title": "Connecting Frontend (React) with Backend (Flask API)",
      "technology": "React.js, Flask, Axios/Fetch API",
      "duration": 2,
      "perquisites": ["React.js Basics", "Flask RESTful APIs"],
      "difficulty_level": 4.0,
      "depth": 1,
      "topic": "Fullstack Integration",
      "is_category": true,
      "importance_score": 98,
      "study_hours_per_day": 10800,
      "description": "Integrating the React frontend with the Flask RESTful API. This involves making HTTP requests from React to Flask, handling data exchange (JSON), and managing Cross-Origin Resource Sharing (CORS) issues.",
      "step_type": "required",
      "free_resources": [
        {
          "name": "Integrating React with a Flask Backend: Best Practices and Common Pitfalls",
          "url": "https://www.section.io/engineering-education/integrating-react-with-flask-backend/",
          "type": "tutorial"
        },
        {
          "name": "How to Connect ReactJS with Flask API (GeeksforGeeks)",
          "url": "https://www.geeksforgeeks.org/how-to-connect-reactjs-with-flask-api/",
          "type": "tutorial"
        }
      ],
      "paid_resources": [
        {
          "name": "Build a Bank: Full-Stack App Development Using React & Flask",
          "url": "https://www.udemy.com/course/build-a-bank-full-stack-app-development-using-react-flask/",
          "type": "course",
          "platform": "Udemy"
        },
        {
          "name": "Building Full-Stack Apps with Flask and React (Intermediate)",
          "url": "https://www.wilco.com/challenges/building-full-stack-apps-with-flask-and-react-intermediate/",
          "type": "course",
          "platform": "Wilco"
        }
      ]
    }
  ]
}
"""
