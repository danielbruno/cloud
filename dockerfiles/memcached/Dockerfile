FROM centos:latest
MAINTAINER Daniel Bruno <danielbrunos@gmail.com>

RUN yum install memcached -y
EXPOSE 11211
CMD ["-l", "0.0.0.0", "-d"]
USER memcached
ENTRYPOINT memcached
