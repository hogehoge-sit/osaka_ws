#include<iostream>
#include<random>
#include<ctime>
using namespace std;




int main(void){
    int N;
    random_device rnd;
    mt19937 mt(rnd());
    uniform_real_distribution<double> score(0.0, 1.0);
    double x, y, cir=0.0;     //乱数を格納する

    cout << "N = ";
    cin >> N;
    for (int i=0; i<N; i++){
        x = score(mt);
        y = score(mt);
        if(x*x + y*y < 1.0){
            cir += 1.0;
        }
    
    }
    double pi = 4*cir / (double)N;
    cout << "Pi = " << pi << endl;


    return 0;
}