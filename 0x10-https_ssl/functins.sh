#!/bin/bash
#checks if shadow file exists
function test_shadow(){
	echo $1
	if [ -e /etc/shadow ]; then
		echo "Shadow file exists";
	else
		echo "Shadow file doest not exist";
	fi
	test_passwd
}

#checks if passwd exists
function test_passwd(){
	if [ -e /etc/passwd ]; then
		echo "Passwd file exists"
	else
		echo "passwd file does not exist"
	fi
}

test_shadow "***Mwaura's script***"
test_shadow "*******Run 2********"
test_shadow "*******Run 3********"
test_shadow "*******Run 4********"
test_shadow "*******Run 5********"
