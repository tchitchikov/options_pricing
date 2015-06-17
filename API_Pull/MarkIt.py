__author__ = 'John'
"""
this will looks at the markit lookup api to pull in the data for stock quotes
"""


class DataPull:
    def stock_quote_api(self):
        """
        This takes in a list of stocks from a predefined file, makes the
        RESTful request for a JSON object and prints it out for now.

        Args:
            stock_list(list): calls the method that parses a stocks file
            rest_json_request_url(string): the RESTful connection string
            stockquoterequest(json): the result of requests RESTful request

        Returns:
            TODO: will return the results as a dict of dicts

        """
        import requests
        stock_quote_request_list = []
        stock_list = self.list_of_stocks()
        for stock in stock_list:
            rest_json_request_url = "http://dev.markitondemand.com/Api/" \
                                    "v2/Quote/json?symbol=" + stock
            stock_quote_request_list.append((requests.get(rest_json_request_url)).text)
        return stock_quote_request_list

    def list_of_stocks(self):
        """
        This reads a list of stocks from a file, parses them and returns them

        Args:
            list_of_stocks_file(io.TextIOWrapper): reads in the file as an IO
            all_stocks(list): a list of all lines in the file
            list_of_stocks(list): where we'll store our return list

        Returns:
            list_of_stocks(list): a list of stocks to examine later

        """
        list_of_stocks_file = open(
            'C:/Users/John/Desktop/list_of_stocks.txt', 'r')
        all_stocks = list_of_stocks_file.readlines()
        list_of_stocks = []
        for stock in all_stocks:
            list_of_stocks.append(stock.strip())
        return list_of_stocks



if __name__ == "__main__":
    markit = DataPull()
    markit.stock_quote_api()
