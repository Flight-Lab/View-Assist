import requests, re
@service(supports_response="optional")
def search_wikipedia(searchterm=None, language="en", return_response=True):
    """yaml
    name: View Assist Search Wikipedia
    description: Search Wikipedia using searchterm in the specified language
    fields:
        searchterm:
            description: What to search for?
            example: Madonna
            required: true
            selector:
                text:
        language:
            description: Language code for the Wikipedia edition (e.g., 'en' for English, 'it' for Italian)
            example: en
            required: false
            default: en
            selector:
                text:
    """
    # Construct the URL with the specified language
    url = f"https://{language}.wikipedia.org/api/rest_v1/page/summary/{searchterm.replace(' ', '_')}?redirect=true"
    r = task.executor(requests.get, url)

    if r.status_code == requests.codes.ok:
        wiki_data = r.json()
        type = wiki_data['type']
        title = wiki_data['title']
        try:
            thumbnail = wiki_data['thumbnail']['source']
        except:
            thumbnail = ""
        full_extract = wiki_data['extract']
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', full_extract.strip())

        # Get the first two sentences
        extract = ' '.join(sentences[:2])

        response_variable = {"type": type, "title": title, "thumbnail": thumbnail, "extract": extract}
        return response_variable
    else:
        response_variable = {"error": r.status_code, "data": r.json()}
        return response_variable
