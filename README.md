# IELTS Listening Training

### How to install

```
git clone https://github.com/scor2k/ielts_listening_training.git
cd ielts_listening_training && python3 -m venv env  && source env/bin/activate 
pip3 install -r requirements.txt && pip3 install -e .
```

### How to run
```
./run --help
./run dates --amount=5 --weekday
./run digits --amount=10 --min 10 --max=100
```

### Changelog

*0.2.0*
 - added prepositions to digits
 - added min param for digits
 - special param for asking weekday when testing dates

*0.1.0* 
 - initial release
