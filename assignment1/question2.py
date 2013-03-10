def parse_links_regex(filename):
    """question 2a

    Using the re module, write a function that takes a path to an HTML file
    (assuming the HTML is well-formed) as input and returns a dictionary
    whose keys are the text of the links in the file and whose values are
    the URLs to which those links correspond. Be careful about how you handle
    the case in which the same text is used to link to different urls.
    
    For example:

        You can get file 1 <a href="1.file">here</a>.
        You can get file 2 <a href="2.file">here</a>.

    What does it make the most sense to do here?
    """
    import re
    
    input = open(filename, "r").read()
    parsed = re.findall(r'<a href="(.*?)".*>(.*)</a>', input)
    
    dict = {}

    for link, text in parsed:
        if text in dict:
            dict[text] += " , " + "%s: %s" % (text, link)
        else:
            dict [text] = "%s" % (link)
    
    return dict


def parse_links_xpath(filename):
    """question 2b

    Do the same using xpath and the lxml library from http://lxml.de rather
    than regular expressions.
    
    Which approach is better? (Hint: http://goo.gl/mzl9t)
    """
    
    # I get an error when I import this that says: ImportError: No module named lxml.html
    # However, I did in fact install it! Thus, I have not been able to test this code...
    from lxml import html

    input = lxml.html.parse(filename)
    links = input.xpath('//tr/td/a/text()')
    print links