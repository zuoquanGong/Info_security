#include<iostream>
#include<vector>
using namespace std;
#define NUM 26
#define FLAG 1
vector<char> Reader(char *filename)
{
	int flag=FLAG;
	FILE *fin=fopen(filename,"r");
	vector<char> stringbuf;
	if(fin==NULL)
	{
		printf("ERROR:文件输入错误\n");
		exit(0);
	}
	while(!feof(fin))
	{
		char c=fgetc(fin);
		stringbuf.push_back(c);
	}
	fclose(fin);
	if(flag==1)
	{
		cout<<"origintext show:\n";
		for(vector<char>::iterator iter=stringbuf.begin();iter!=stringbuf.end();iter++)
			cout<<*iter;
		cout<<endl<<endl;
	}
	return stringbuf;
}
void convert(vector<char> &clrtext,int key)
{
	for(int i=0;i<clrtext.size();i++)
	{
		if(clrtext[i]>=65&&clrtext[i]<=90)
		{
			clrtext[i]-=65;
            clrtext[i]=(clrtext[i]+key)%26+65;
		}
		else if(clrtext[i]>=97&&clrtext[i]<=122)
		{
			clrtext[i]-=97;
			clrtext[i]=(clrtext[i]+key)%26+97;
		}
	}
	return;
}
void unconvert(vector<char> &clrtext,int key)
{
    for(int i=0;i<clrtext.size();i++)
	{
		if(clrtext[i]>=65&&clrtext[i]<=90)
		{
			clrtext[i]-=65;
            clrtext[i]=clrtext[i]-key%26;
			if(clrtext[i]<0)
				clrtext[i]=26+clrtext[i]+65;
			else
				clrtext[i]=clrtext[i]+65;
		}
		else if(clrtext[i]>=97&&clrtext[i]<=122)
		{
			clrtext[i]-=97;
			clrtext[i]=clrtext[i]-key%26;
			if(clrtext[i]<0)
				clrtext[i]=26+clrtext[i]+97;
			else
				clrtext[i]=clrtext[i]+97;
		}
	}
	return;
}
void show_ciphertext(vector<char> ciphertext)
{
	for(int i=0;i<ciphertext.size();i++)
		cout<<ciphertext[i];
	cout<<endl;
}
void save_ciphertext(vector<char> ciphertext,char *out)
{
	FILE *fout=fopen(out,"w");
    for(int i=0;i<ciphertext.size();i++)
		fputc(ciphertext[i],fout);
	fclose(fout);
}
int main(int argc,char **argv)
{
	//cout<<argc<<endl;
	vector<char> text;
	char *help="-help";
	if(strcmp(argv[1],help)==0)
	{
		printf("第一个参数为密钥（正整数值）\n");
		printf("第二个参数为模式（加密--1，解密--0）\n");
		printf("第三个参数为待处理文件名（默认名“cleartext.txt”）\n");
		printf("第四个参数为输出文件名（默认名“out.txt”）\n");
		exit(0);
	}
	if(argc<3)
	{
		printf("ERROR:控制台输入错误\n");
		exit(0);
	}
	if(argc>=4)
		text=Reader(argv[3]);
	else
		text=Reader("cleartext.txt");

	for(int i=0;i<strlen(argv[1]);i++)
	{
		if(argv[1][i]<49||argv[1][i]>57)
		{
			printf("ERROR:控制台输入错误\n");
			exit(0);
		}
	}
	int key=atoi(argv[1]);
	if(argv[2][0]=='1')
	{
	    convert(text,key);
	}
    else if(argv[2][0]=='0')
	{
		unconvert(text,key);
	}
	else
	{
	    printf("ERROR:控制台输入错误\n");
		exit(0);
	}
	show_ciphertext(text);
	char out[NUM]="out.txt";
	if(argc>=5)
	{
		strcpy(out,argv[4]);
	}
	//cout<<"We will save the file as "<<out<<endl;
	save_ciphertext(text,out);
	return 0;
}