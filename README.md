# lyft_cut_string

This application;
accepts a POST request to the route “/test”, which accepts one argument “string_to_cut”
then, returns a JSON object with the key “return_string” and a string containing every third letter from the original string

(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.
