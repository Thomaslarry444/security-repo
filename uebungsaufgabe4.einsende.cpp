#include <iostream>
using namespace std;
class Kreis; 
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
class Kreis{
	private:
		float radius,xm,ym;
	public:
		Kreis(float x, float y,float r){xm=x;ym=y;radius=r;}
		Kreis(float r ){radius=r;xm=0;ym=0;}
		~Kreis(){}
		void setze_Mittelpunkt(float x, float y){xm=x;ym=y;}
		void setze_Radius(float r){radius=r;}
		float erhalte_xm(){return xm;}
		float erhalte_ym(){return ym;}
		float erhalte_radius(){return radius;}
		float durchmesser (){return 2*radius;}
		float umfang (){return 2*3.14*radius;}
		float flaeche (){return 3.14*radius*radius;}
		void ausgabe (){cout<<"\n Mittelpunkt M("<<xm<<","<<ym<<"); Radius r= "<<radius<<endl;
		}
	
};
int main() {
	Kreis k1 (3.1f);
	cout<<"Kreis k1:"<<endl;
	k1.ausgabe();
	cout<<"Durchmesser: "<<k1.durchmesser()<<endl;
	cout<<"Flaeche: "<<k1.flaeche()<<endl;
	cout<<"Umfang: "<<k1.umfang()<<endl;
	Kreis k2(5.5 , 1.2 , 4.1);
	cout<<"\nKreis k2:"<<endl;
	k2.ausgabe();
	k2.setze_Mittelpunkt(0.5,0.5);
	k2.ausgabe();
	cout<<"Flaeche: "<<k2.flaeche()<<endl;
	cout<<"Umfang: "<<k2.umfang()<<endl;
	return 0;
}


