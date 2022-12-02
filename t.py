import wordninja

wikipages = ['4kworkflow', 'basicsofscreenrecording', 'bettertechsupport', 'codecsandcontainers', 'config/description', 'config/sidebar', 'config/stylesheet', 'config/submit_text', 'config/welcome_message', 'divideandconquer', 'drives', 'faq', 'faq/analogcapture', 'faq/audio_limitations', 'faq/chromakeying', 'faq/editingtools', 'faq/fasterpremiereoutput', 'faq/filesize', 'faq/gettingstarted', 'faq/h264ishard', 'faq/hardware_vs_software_encoding', 'faq/laptops', 'faq/learnediting', 'faq/macandpcfilesizes', 'faq/masking', 'faq/matchmoving', 'faq/multibandcompressor', 'faq/proxies', 'faq/resources', 'faq/rotoscoping', 'faq/upscaling-and-other-myths', 'faq/vfr', 'faq/vhslook', 'faq/where_should_i_learn', 'ffmpeg', 'index', 'index/fair_use', 'index/understanding_compression', 'index/videoeditingsoftware', 'index/videoeditingsoftware/why_wondershare_gets_a_bad_rap', 'premierecpugpuusage', 'quote_supercuts_and_more', 'submissionrules', 'tech/color', 'tech/interframe', 'tech/techsupport_howto', 'that_dance_video', 'unbake_a_cake', 'vhs-like_look']

allowed_wikipages = [i for i in wikipages if 'config' not in i]

for wikipage in allowed_wikipages:
    wikipage = ' '.join(wordninja.split(''.join(wikipage.split('/')[-1])))
    print(wikipage.title())
