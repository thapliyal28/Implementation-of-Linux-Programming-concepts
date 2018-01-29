
#include <iostream>
#include <cstring>
using namespace std;

/*-------------------function to input path between vertices---------------------------------*/


void edges(int ver, char *one, int &fl)
{
    
    string s;
    char delimiter[] = "{";
    char delim[]="}";
    char *splitted, *secsplitted;
    int fdigit, sdigit;
    std::getline (std::cin,s);
    cout<<"E ="<<s<<"\n";//added
    


if(s.length()<=4)   // for a e {} condition.
{ 

return;                    
}


else
{

    char *str= const_cast< char *>(s.c_str());  // changing str to char * ,for strtok to work.
    strtok(str, delimiter);
    splitted = strtok(NULL, delim);
    secsplitted = strtok(splitted, ",");


    while (secsplitted != NULL) 
	{

        fdigit = atoi(&secsplitted[1]);
        secsplitted = strtok(NULL, ",");
        sdigit = atoi(secsplitted);

        if (fdigit < 0 || fdigit >= ver || sdigit < 0 || sdigit >= ver) 
	{
            cerr<<"Error: the pair <"<<fdigit<<","<<sdigit<<"> is invalid.Please write correct valid pair\n";
	    fl=0;  
	    
        } 
	else 
	{
            one[fdigit * ver + sdigit] = 1;
            one[sdigit * ver + fdigit] = 1;
        }

        secsplitted = strtok(NULL, ",");
    }

}

}
/*---------------------BFS-----------------------------*/
void algo(int V, char *one, int check[], int first, int second)
{

    int i, j;
    int *queue;
    int len = 0;

    queue = (int *)::operator new(sizeof(int) * V);
    if (queue == NULL) 
	{
        cerr<<"Error: Memory allocation problem.\n";
        exit(-1);
    	}

    check[first] = first;
    queue[len ++] = first;
    for (i = 0; i < len; i++)
	{

        	int curr = queue[i];

        	if (curr == second) 
		{

         	   break;
        	}


        	for (j = 0; j < V; j++) 
		{
            	if (one[curr * V + j] && check[j] == -1)
            	{

               	 check[j] = curr;
                 queue[len ++] = j;
            	}
       	        }
       }
     ::operator delete(queue);
}


//path recovery for the final path
/*-------------------------path recovery-------------------------*/
void path(int check[], int des)
{
    if (check[des] == des)
	 {
        cout<< des;
    	  } 
	else 
	{
        path(check, check[des]);
        cout<<"-"<< des;
         }
}


/*----------------------------main------------------------------------*/
 
int main()
{
    long int vertex;
    char *one = NULL;
    int *check = NULL;
    int fl=0;

    int first, second;
    char test[2];
    while (cin>>test)
    {
	
        char a = test[0];
        switch (a) {

            case 'V':
            case 'v':

                cin>>vertex;
                if (vertex < 0) 
			{
                    cerr<<"Error: number of vertices must be positive.\n";
                    break;
                	}
                else
                {
			
                    if (one != NULL)
                    {
                        ::operator delete(one);
                        ::operator delete(check);
                    }
		    
		    cout<<"V = "<<vertex<<"\n";//added for printing v.
                    one = (char *) ::operator new(sizeof(char) * vertex * vertex);
                    check = (int *) ::operator new(sizeof(int) * vertex);
                    if (one == NULL || check == NULL) 
			{
                        cerr<<"Error: memory allocation problem.\n";
                        exit(-1);
                   	 }
                }
                break;

            case 'E':
            case 'e':
		
		
		/*
                fl=fl+1;

		if(fl==1)

		{
                memset(one, 0, vertex * vertex);//copies 0 to first v*v memory spaces of one
                edges(vertex, one,fl);
		break;
		}

		else
		{


		cerr<<"Error:Only one E command is allowed after v and should contain all paths. \n";
		break;
		
		
		}*/


		memset(one, 0, vertex * vertex);//copies 0 to first v*v memory spaces of one
                edges(vertex, one,fl);
		break;


            case 's':
            case 'S':
			
		fl=0;

                cin>>first>>second;
		
		

                if (first < 0 || first >= vertex || second < 0 || second >= vertex) 
		{
                    cerr<<"Error: vertices are out of range.\n";
                    break;
                }

                memset(check, -1, sizeof(int) * vertex);//copies -1 to first v memory spaces of check.
                algo(vertex, one, check, first, second);

                if (check[second] == -1) 
		{

                    cerr<<"Error: There is no path between"<<" "<< first <<","<< second<<"\n";
                } 


		else 
		{
                    path(check, second);
                    cout<<"\n";
                }
                break;

	default:
                cerr<<"Error: Invalid input \n";
        }
	
    }
    if (one != NULL)
    {
        ::operator delete(one);
        ::operator delete(check);
    }
    return 0;
}





