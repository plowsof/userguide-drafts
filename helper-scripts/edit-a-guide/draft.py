import os
import textwrap
import pprint
import glob 

feed_1_str = "Run monerod by typing the following, replacing"
feed_2_str = "[Service] Type=forking PIDFile=/home/<username>/monerod.pid"
feed_3_str = "That's it! Do not replace the dsc****.b32.i2p address with yours, only"
feed_1 = 0
feed_2 = 0
feed_3 = 0
replace_string = "--add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p "
feed_1_text = ""
feed_2_text = ""
feed_3_text = "Note: monerod versions v0.17.1.3 onwards comes with a list of hardcoded monerod peers accessible via I2P which are used to then discover further I2P peers. You can manually add peers to the list by passing `--add-peer` flags to the `monerod` command above. E.g. `--add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p`"
feed_1_write = 0
feed_2_write = 0
feed_3_write = 0

def feed_1_wrap(text):
    global replace_string
    text = text.replace(replace_string,"")
    text = text.replace("--anonymous-inbound", "lolwhyyyyyyyyyyyyyyy").replace("--tx-proxy", "hehelolom") #textwrap does not like --??-??..
    text = textwrap.fill(text, 75).replace("lolwhyyyyyyyyyyyyyyy","--anonymous-inbound").replace("hehelolom","--tx-proxy").split("\n")
    return text


def edit_po_file(in_file):
    with open(in_file) as f:
        lines = f.readlines()

    do_write = 1
    with open("new_data.po","w+") as f:
        for line in lines:
            if feed_1_str in line:
                do_write = 0
                feed_1 = 1
            if feed_2_str in line:
                do_write = 0
                feed_2 = 1
            if feed_3_str in line:
                do_write = 0
                feed_3 = 1
            if feed_1 == 1:
                if line != "msgstr \"\"\n":
                    if feed_1_write == 1: 
                        if line == "\n":
                            #possible no translation so feed_1_text is empty
                            if feed_1_text != "":
                                feed_1_text = feed_1_wrap(feed_1_text)
                                for l in feed_1_text:
                                    f.write(f"\"{l} \"\n")
                            feed_1 = 0
                            do_write = 1
                        else:
                            feed_1_text += line.replace("\"","").replace("\n","")
                    else:
                        feed_1_text += line.replace("\"","").replace("\n","")
                else:
                    if feed_1_write == 0:
                        feed_1_text = feed_1_wrap(feed_1_text)
                        for l in feed_1_text:
                            f.write(f"\"{l} \"\n")
                        f.write(line)
                        feed_1_text = ""
                        feed_1_write = 1
            if feed_2 == 1:
                if line != "msgstr \"\"\n":
                    if feed_2_write == 1: 
                        if line == "\n":
                            #possible no translation so feed_1_text is empty
                            if feed_2_text != "":
                                feed_2_text = feed_1_wrap(feed_2_text)
                                for l in feed_2_text:
                                    f.write(f"\"{l} \"\n")
                            feed_2 = 0
                            do_write = 1
                        else:
                            feed_2_text += line.replace("\"","").replace("\n","")
                    else:
                        feed_2_text += line.replace("\"","").replace("\n","")
                else:
                    if feed_2_write == 0:
                        feed_2_text = feed_1_wrap(feed_2_text)
                        for l in feed_2_text:
                            f.write(f"\"{l} \"\n")
                        f.write(line)
                        feed_2_text = ""
                        feed_2_write = 1
            if feed_3 == 1:
                print(line)
                if line != "msgstr \"\"\n":
                    if feed_3_write == 1: 
                        if line == "\n":
                            do_write = 1
                else:
                    if feed_3_write == 0:
                        feed_3_text = feed_1_wrap(feed_3_text)
                        for l in feed_3_text:
                            f.write(f"\"{l} \"\n")
                        f.write(line)
                        feed_3_text = ""
                        feed_3_write = 1
            if do_write == 1:
                f.write(line)

    # delete in_file
    # copy new_data to in_file

def replace_md_files():
    global replace_string
    lang = ["nl","pt-br","nb-no","de","it","tr","pl","ru","en","fr","ar","es","zh-cn","zh-tw"]
    for l in lang:
        fname = f"./monero-site/_i18n/{l}/resources/user-guides/node-i2p-zero.md"
        if not os.path.isfile(fname):
            continue
        print(l)
        with open(fname,"r") as f:
            lines = f.readlines()
        for line in lines:
            if replace_string in line:
                line = line.replace(replace_string, "")

replace_md_files()
