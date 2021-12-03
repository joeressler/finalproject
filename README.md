So, basically in order to run this program you need to do a few things first.

First, open up config_writer.py, mess with the dictionary's weightings to whatever your minigame ingredient's weightings are, and then run it, creating your new config_uuid file.

I would keep track of this file's name via clipboard because uuids tend to be very obviously easy to memorize.... not

Once you've done that, open up simulator.py in either your terminal or interactive window (VSCode gang rise up) and you will meet some input() prompts.

First prompt will ask you how many times to run your sim, just input however many, don't get too big or it will break (I don't actually know if it breaks, I just haven't had the time to test it running for that long so I'm running with the assumption that it breaks)

Boom, you're done. The code *should* output all your averages and upper outlier. You can mess with overlord.py to print different results, but be careful with changing things/printing things in the lower files.
