FROM amazon/aws-lambda-python

RUN pip install --upgrade pip
RUN pip install poetry

RUN curl -fsSL https://rpm.nodesource.com/setup_14.x | bash - && yum install -y nodejs

ENV POETRY_VIRTUALENVS_IN_PROJECT=true