# W2D1-Assignment-FS-S24-Web-Development

## This assignment is due Fri March 8 @ 11:59PM EST

This assignment is designed to reinforce your understanding of making API requests, handling responses, and working with different serialization methods.

## Part 1: API Testing with curl and Postman

### Task 1: curl Scripting

Installation Instructions (curl):
- If you're using a Unix-based system like Linux or macOS, `curl` is likely already installed. You can verify by opening a terminal and typing `curl --version`. If it's not installed, you can typically install it through your package manager (e.g., `sudo apt install curl` on Ubuntu).
- For Windows users, `curl` can be installed by downloading the executable from the official website and adding it to your system PATH.

Task Instructions:
1. Create a new script file named `post-request.sh`.
2. Use `curl` to make a POST request to the ([JSONPlaceholder API](https://jsonplaceholder.typicode.com))

Refer to the API documentation for details on the endpoint.
3. Execute the script and capture the response.

### Task 2: Postman Collection

Installation Instructions (Postman):
- Download and install the Postman application from the official website ([https://www.postman.com/downloads/](https://www.postman.com/downloads/)).

Task Instructions:
1. Launch Postman after installation.
2. Create a new collection.
3. Add a request to the collection for making a POST request to the same JSONPlaceholder endpoint.
4. Set up any necessary headers or parameters.
5. Execute the request and capture the response.

Pushing Postman Files to GitHub:
- Export your Postman collection as a JSON file.
- Initialize a Git repository in your project directory (`git init`).
- Add the exported Postman JSON file to your project (`git add filename.json`).
- Commit the file to your local repository (`git commit -m "Add Postman collection"`).
- Create a new repository on GitHub if you haven't already.
- Add your local repository as a remote (`git remote add origin <repository-url>`).
- Push your commits to GitHub (`git push -u origin master`).

## Part 2: Serialization

### Task 3: JSON Serialization in JavaScript

Task Instructions:
1. Create a JavaScript file named `serialize-json.js`.
2. Define a simple JavaScript object with key-value pairs representing information about a book.
3. Use `JSON.stringify()` to serialize the object into a JSON string.
4. Log the serialized JSON string to the console.

### Task 4: gRPC Exploration

Installation Instructions (gRPC):
- Choose your preferred programming language (e.g., Python, Java, Go) for working with gRPC.
- Install the necessary tools and libraries for gRPC development in your chosen language. This may include language-specific gRPC libraries and the Protocol Buffers compiler (`protoc`).

Task Instructions:
1. Research and install the necessary tools to work with gRPC in your preferred programming language.
2. Create a simple gRPC service and client that exchange a basic message.
3. Execute the gRPC service and observe the communication between the service and client.

## Submission Instructions

- Organize your assignment into a directory structure with separate folders for each task.
- Include a README file summarizing your approach, any challenges faced, and key learnings.
- Create a GitHub repository containing all the assignment files and submit.


