# whatsapp_bulk_check
Check links for WhatsApp groups in bulk.


This Python script is designed to automate the verification of WhatsApp links in bulk. It utilizes multiple threads to concurrently process multiple URLs, checks for the existence of a specific element on each webpage, and presents the results in the console while saving them to a specified output file.

## Prerequisites

Make sure to have the following libraries installed before running the script:

- `requests`: An HTTP library for making requests.
- `colorama`: A library for adding color to text in the terminal.
- `beautifulsoup4`: A library for extracting data from HTML and XML files.
- `concurrent.futures`: A library for concurrent execution (typically included in the standard Python library).

You can install them using the following command:

bash

`pip install requests colorama beautifulsoup4`

---

## Usage

1. Run the script in a Python 3 environment.
2. Choose one of the text files containing the URLs you want to verify.
3. Input the number corresponding to the desired file when prompted.
4. Specify the desired number of threads for concurrent processing.
5. Provide the name of the output file to save the results.
6. Wait for the script to process the URLs, and observe the results in the console.


## Example Output

The script will provide real-time feedback in the console and save the results in the specified output file. The results will indicate whether the specific element was found on each URL or if an error occurred during the request.

```
[ ✔️ ] disponível ~ https://chat.whatsapp.com/103gmaFldet3alR1levheq: Grupo Maneiro
[ ✖️ ] inexistente ~ https://invalidurl.com: Error accessing URL https://erroredurl.com. Details: Error message.
Resultados salvos em tempo real em saida.log
```

## Notes

- In case of errors during URL requests, the script will provide details about the error.
- The number of threads can be adjusted to optimize processing speed, but avoid choosing extremely high numbers.

This script was developed by [Gato](https://www.instagram.com/gato.ads/). If you need assistance or have questions, feel free to reach out!
