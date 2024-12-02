# static_site_generator

#<html> is the root element of the document.
    <head> contains metadata about the document. Anything in the <head> is not rendered visibly in the browser window.
    <title> is the title of the document, which is displayed in the browser tab.
    <body> contains the content of the document, which is what is rendered in the browser window.
    <h1> is a top-level heading.
    <p> is a paragraph of text.
    <a> is a hyperlink. The href attribute is the URL the link points to. Attributes are key-value pairs that provide additional information about an element, like href="https://www.boot.dev".

# CSS (Cascading Style Sheets)
    a way to dress up your HTML with colors, fonts, responsive layouts, animations, etc.

/* Make all <h1> HTML elements red */
h1 {
  color: red;
}

/* Make all <p> HTML elements 50% of the screen width */
p {
  max-width: 50%;
}

# Primary purpose of this site generator is to convert md to html

# LeafNode a type of HTMLNode that represents a single HTML tag with no children <p> tag with some text inside
    It's a leaf in a tree of HTML nodes
