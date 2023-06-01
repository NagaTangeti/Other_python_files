import openai

def generate_job_listings(skills, location):
  """Generates a list of job listings that match the given skills and location.

  Args:
    skills: A list of strings that represent the desired skills.
    location: A string that represents the desired location.

  Returns:
    A list of job listings.
  """

  # Create a request object.
  request = {
    "prompt": "Find me job listings that match the following skills and location: {} {}".format(skills, location),
    "temperature": 0.7,
    "max_tokens": 100,
  }

  # Generate a response from OpenAI.
  response = openai.api.create(engine="davinci", prompt=request)

  # Extract the job listings from the response.
  job_listings = []
  for job_listing in response["choices"]:
    job_listings.append(job_listing["text"])

  # Return the list of job listings.
  return job_listings

job_listings = generate_job_listings(["mechanical engineer", "mechanical design"], "Newcastle Upon Tyne")
