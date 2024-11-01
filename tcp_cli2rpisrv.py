import socket       # 서버의 IP 주소와 포트 번호 설정
HOST = '0.0.0.0'    # 모든 인터페이스에서 연결을 수신
PORT = 10000        # 포트 번호 (임의로 선택)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # 소켓 생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 소켓 옵션 설정 (포트 사용 후 바로 재사용 가능하도록)
server_socket.bind((HOST, PORT))                # IP 주소와 포트 번호를 소켓에 바인딩
server_socket.listen(1)                         # 클라이언트의 연결을 대기 (최대 1개의 연결 대기)
print(f"Server listening on {HOST}:{PORT}")
conn, addr = server_socket.accept()             # 클라이언트 연결 수락
print(f"Connected by {addr}")
try:                # 데이터를 계속 수신 (연결이 끊어질 때까지)
    while True:
        data = conn.recv(1024)  # 1024 바이트씩 데이터 수신
        if not data: break
        print(f"Received: {data.decode('utf-8')}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:            # 연결과 소켓 닫기
    conn.close()
    server_socket.close()
    print("Connection closed")
