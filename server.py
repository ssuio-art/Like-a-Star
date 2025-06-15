from livereload import Server, shell
import os

# 設定根目錄
root_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(root_dir)

# 建立伺服器
server = Server()

# 監視所有相關檔案的變更
server.watch('*.html', shell('echo "HTML file changed"'))
server.watch('*.js', shell('echo "JavaScript file changed"'))
server.watch('*.css', shell('echo "CSS file changed"'))

print(f'伺服器已啟動在 http://localhost:8000')
print('正在監視檔案變更...')
print('按 Ctrl+C 可以停止伺服器')

# 設定伺服器
server.serve(port=8000, host='localhost', root=root_dir) 