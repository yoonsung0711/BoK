# [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576) (해시)
>  해시에 구현된 주요 메소드의 시간 복잡도는 O(1)임.  
>  따라서 해시 문제는 시간 복잡도 요건이 까다로울 수 있음.  
    
### 코드
- [실패](an_unfulfilled_player_double_loop.py) :  double loop 시간 초과
- [성공](an_unfulfilled_player_hash.py) : hashmap 정확성, 효율성 만족

### 보충자료
- [Hash, Hashing, Hash Table(해시, 해싱 해시테이블) 자료구조의 이해](https://velog.io/@cyranocoding/Hash-Hashing-Hash-Table%ED%95%B4%EC%8B%9C-%ED%95%B4%EC%8B%B1-%ED%95%B4%EC%8B%9C%ED%85%8C%EC%9D%B4%EB%B8%94-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EC%9D%98-%EC%9D%B4%ED%95%B4-6ijyonph6o)

# [탑](https://programmers.co.kr/learn/courses/30/lessons/42588) (스택 / 큐)
> pop이 구현된 list는 곧 스택과 같음.  
> 스택과 큐에 구현된 주요 메소드의 시간 복잡도는 O(1)임.  
> 중첩 순회 시 순회 대상의 원소 개수가 순회시마다 감소하는 경우 스택-pop으로 치환하여 코드를 간결하게 표현할 수 있으나 성능 차이는 거의 없음.  

### 작성한 코드
- [성공](tower_double_loop.py) : 스택 / 큐를 사용하지 않은 코드 
- [성공](tower_stack.py) : 스택 / 큐로 치환한 코드

### 보충자료
- [자료구조 - 스택(Stack)](http://blog.naver.com/PostView.nhn?blogId=justkukaro&logNo=220503515118)

-----
![Data Structure Operations](DataStructureOperations.png)