
class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag  #string representing HTML tag name p, h1, a
        self.value = value #string representing value of HTML tag, text inside paragraph
        self.children = children #list of HTMLNode objects that are the children of this node
        self.props = props  #dictionary representing attributes of HTML tag, <a> tag has {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_dict = self.props.items()
        prop_list = []
        for prop in prop_dict:
            prop_list.append(f' {prop[0]}="{prop[1]}"')
        return "".join(prop_list)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
    def __eq__(self, tar):
        return (
            self.tag == tar.tag
            and self.value == tar.value
            and self.children == tar.children
            and self.props == tar.props
        )
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent needs tag")
        if self.children == None or len(self.children) == 0:
            raise ValueError("Parents have children")
        children_tag = ""
        for child in self.children:
            children_tag += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_tag}</{self.tag}>'
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
                             
