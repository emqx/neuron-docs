# Start development

## Branch

This project has a main branch, `main`. Please ensure that `main` is compiled and usable at any time. At the same time, there are branches corresponding to different versions of this project, and you can choose your own branches for development.

## Modify Code

For functional issues, please submit at least one test case to verify changes to existing functionality; For performance related issues, please submit necessary test data to prove the performance defects of existing code or the performance improvement of new code.
Please perform tests before each push.

### Unit testing

Run all unit tests

```shell
$ cd build
$ ctest --output-on-failure
```

### Functional testing

Run all functional tests

```shell
$ sudo apt-get install -y mosquitto
$ mosquitto -v &
$ python3 -m pip install -U pip
$ python3 -m pip install -r ft/requirements.txt
$ python3 -m robot --maxerroelines=600 -P ft/ -d ft/reports ft
```

## Pull Request

* A PR only does one thing. If there are multiple bug fixes, please submit a PR for each bug;
* The PR process is as follows:

  * First, fork this project and create your own github.com/your/neuron warehouse;
  * Clone your own Neuron warehouse to the local location:
  ```bash
  $ git clone https://github.com/your/neuron.git 
  ```
  * For example, create a new branch based on the `main` branch;
  * Make changes on the newly created branch and submit the changes;
  * Before pushing the modified branch to your own warehouse, switch to the `main` branch and run the following command to pull the latest remote code:
  ```bash
  $ git pull https://github.com/emqx/neuron.git
  ``` 
  * If the new remote code is retrieved in the previous step, switch to the previously created branch and run branch merge operation.
  ```bash
  $ git rebase main
  ```
  If you encounter a file conflict, you need to resolve the conflict;
  * After the previous step is completed, you can push the branch you created to your own warehouse:
  ```bash
  $ git push origin main
  ```
  * Finally, send a PR to the corresponding branch of emqx/neuron from the newly pushed branch of your warehouse;

* Provide a complete description of the problems solved/new features added/the intent of the modifications made to the code in the title and text of the PR;
* Wait patiently for the developer's response, and we will respond soon.