# console blog generator
# very wip

"""
console.log("text","style")
"""

#initial html
html = """
<html>
<head></head>
<body>
<p> this blog isnt here  </p>
<script src="index.js">
</script>
</body>
</html>
"""

#initial js
js = """

"""
#commands
action = input("what do you want do to? (create) blog , (add) post , (view) posts , (remove) post or (edit) post ?")
match action:
  case create: 
    f = open("index.html", "at")
    f.write(html)
    f.close()
    g = open("index.js", "at")
    g.write(js)
    g.close()
  case add:
    h = open("demofile2.txt", "at")
    title = input("type below post title text")
    post = input("type below post content text")
    h.write('console.log(',title,'); console.log(',content,');')
    h.close()
  case remove:
    input("which number of post to remove ?")
  case edit:
    input("which number of post to edit ?")
  case view:
    
