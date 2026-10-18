# src/app.html の <!--JSPDF--> に vendor/jspdf を埋め込んで index.html を作る
import pathlib
root=pathlib.Path(__file__).parent
s=(root/'src/app.html').read_text(encoding='utf8')
lib=(root/'vendor/jspdf.umd.min.js').read_text(encoding='utf8').replace('</script','<\\/script')
assert '<!--JSPDF-->' in s
(root/'index.html').write_text(s.replace('<!--JSPDF-->','<script>'+lib+'</script>'),encoding='utf8')
print('built index.html')
