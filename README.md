# Fine Tuning using qLora at the Fugaku-LLM
This is an small chatgpt to the japanese using fugaku llm.

    https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct-gguf

    https://zenn.dev/hellorusk/articles/94bf32ea09ba26

## Creating a virtual environment in Python and we will install Ollama to run Fugaku LLM:
Article where I based

    https://tech.takuyakobayashi.jp/2024/05/18/23#google_vignette

    https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/

    https://zenn.dev/if001/articles/6c507e15cd958b

    https://note.com/npaka/n/n79eebc29366d

    https://ollama.com/blog/run-llama2-uncensored-locally

    https://www.silasreinagel.com/blog/ai/llama2/llm/2024/03/14/ai-how-to-run-llama-2-locally/

1. Checking python version:

        python --version or python3 --version

2. Checking if venv installed:

    Usually, Python 3.3 to above the venv comes together.

         python -m venv --help

    If not just install running the following

        sudo apt-get install python3.x-venv

3. Creating an virtual environment:

    Choose the directory that you want to develop and digit the following command

        python -m venv environment_name

4. Activating the virtual environment:

    Window:

         environment_name\Scripts\activate

    MacOs/Linux:

         source environment_name/bin/activate

5. Now, you can install, using pip, fastapi package:

    Before to install packages

        python -m pip install --upgrade pip

    And now, you can install

        pip install -q accelerate==0.26.1 peft==0.4.0 bitsandbytes==0.42.0 transformers==4.36.2 trl==0.4.7 datasets==2.16.1

    If you have a requirements.txt, just copy it inside of virtual environment directory and run following command

         pip install -r requirements.txt

6. Freeze packages versions on the requirements.txt file:

    After installed packages that you need to your project is a good practice to freeze its in a requirements.txt files.

    To do it, you have, in first, digit

        pip freeze

    After this you have to create a requirements file and to make Ctrl+C and Ctrl+V about this file. Or, more fast

        pip freeze > requirements.txt

7. (Tip) If you want to get out of the virtual environment just type:

        deactivate

8. Installing Ollama:

        sudo apt-get update

        sudo apt-get install curl

        curl -fsSL https://ollama.com/install.sh | sh

        ollama serve

9. Run Ollama:

    In first place, you have to in at the model directory

        cd model

    In the following to run the command below to read modelfile.txt

        ollama create fugaku -f modelfile.txt

    After this, you can start the ollama

        ollama run fugaku

    TIP: If you need to finish the chat, you just need to type

        /bye

10. Verify ollama's log


        journalctl -u ollama --no-pager

## Creating an Interactive Chat by Ollama:

    https://github.com/ollama-ui/ollama-ui

    https://tech.takuyakobayashi.jp/2024/05/18/23#google_vignette

## References
[1]: https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct
[2]: https://github.com/Fugaku-LLM/DeepSpeedFugaku
[3]: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch
[4]: https://github.com/llm-jp/awesome-japanese-llm
[5]: https://www.nvidia.com/content/DriverDownloads/confirmation.php?url=/Windows/531.61/531.61-desktop-win10-win11-64bit-international-dch-whql.exe&lang=us&type=GeForce
[6]: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.14.4/release-notes.html
[7]: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.14.4/index.html
[8]: https://zenn.dev/hellorusk/articles/94bf32ea09ba26
[9]: https://tech.takuyakobayashi.jp/2024/05/18/23
[10]: https://note.com/owlet_notes/n/nd144bd2d1dc1
[11]: https://note.com/ngc_shj/n/n7a8ce01f13ac
[12]: https://github.com/ollama-ui/ollama-ui
[13]: https://dataloop.ai/library/model/fugaku-llm_fugaku-llm-13b/
[14]: https://huggingface.co/docs/trl/index
[15]: https://github.com/llm-jp/llm-jp-sft
[16]: https://github.com/llm-jp/llm-jp-tokenizer
[17]: https://github.com/llm-jp/llm-jp-dpo
[18]: https://github.com/microsoft/LoRA
[19]: https://github.com/artidoro/qlora
[20]: https://arxiv.org/abs/2305.14314
[21]: https://github.com/microsoft/Phi-3CookBook
[22]: https://arxiv.org/abs/2005.14165
[23]: https://arxiv.org/abs/2201.11903
