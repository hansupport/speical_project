# poject info
숫자 야구 게임의 솔루션을 제공하는 프로그램을 개발한다.

# Bulls And Cows
Bulls And Cows는 숫자 야구 게임으로, 미리 정해져 있는 숫자를 스트라이크와 볼의 개수 정보를 통해 예측하여 맞추는 게임이다.

## Game Rule
1. __*4자리의 임의의 숫자*__ (이하 __*맞출 숫자*__) 가 설정된다.

   > 사용되는 숫자의 규칙 
   > + 사용되는 숫자는 0에서 9까지의 숫자이다.
   > + 사용되는 숫자는 중복되지 않는다. (ex: 1234 (o) / 1111, 1123 (x))
2. 맞출 숫자를 예측하여 4자리의 숫자를 설정한다.
3. 예측한 숫자에서
   + 숫자는 맞지만 위치가 틀리면 볼
   + 숫자와 위치가 둘 다 맞으면 스트라이크
4. 주어진 볼, 스트라이크 정보를 가지고 예측한 숫자가 맞출 숫자와 같을 때까지 2, 3의 과정을 반복한다.