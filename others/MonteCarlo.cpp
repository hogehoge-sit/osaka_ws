/*Pythonでも書いたが、モンテカルロ法による円周率近似。
C++は乱数の生成からしてすでに面倒くさかった、正直まだよくわかっていない。*/

#include<iostream>
#include<random>
#include<ctime>
using namespace std;

int main(void){
    int N;      //乱数の数
    random_device rnd;      //乱数生成デバイスのインスタンスを生成。
    mt19937 mt(rnd());      //メルセンヌツイスターの32bit版によるパラメタ指定。一般にこれが推奨されるらしい。
    uniform_real_distribution<double> rand(0.0, 1.0);  //0~1の範囲の一様実数分布を生成する。
    double x, y, cir=0.0;     //乱数の格納と円内の点を数え上げる。

    cout << "N = ";
    cin >> N;
    for (int i=0; i<N; i++){
        x = rand(mt);
        y = rand(mt);
        if(x*x + y*y < 1.0){
            cir += 1.0;
        }
    
    }
    double pi = 4*cir / (double)N;
    cout << "Pi = " << pi << endl;


    return 0;
}