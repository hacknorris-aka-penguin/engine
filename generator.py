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
<script src="index.js">
</script>
</body>
</html>
"""

#initial js
js = """

"""
#commands
action = input("what do you want do to? (create) blog , (add) post , (remove) post or (edit) post ?")
match action:
  case create: 
    f = open("index.html", "a")
    f.write(html)
    f.close()
    g = open("index.js", "a")
    g.write(js)
    g.close()
  case add:
  case remove:
  case edit:
