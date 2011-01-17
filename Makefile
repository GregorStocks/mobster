default: mobster

mobster:
	cobra -c -files:files.txt -out:bin/mobster.exe -cs:all -ert -cin -debug

clean:
	rm bin/*.exe
