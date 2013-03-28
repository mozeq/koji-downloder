from HTMLParser import HTMLParser
import urllib2

TEST_HTML = '<a href="userinfo?userID=1809">jfilak</a>'

build_sys_urls = {
                "koji":("kojipkgs.fedoraproject.org","/scratch/%s/task_%s"),
                "brew":("download.englab.brq.redhat.com", "/brewroot/scratch/%s/task_%s"),
              }


class Task(HTMLParser):
    global archs

    def __init__(self, task_url):
        HTMLParser.__init__(self)
        self.user = None
        self.ttype = None
        self.tid = None

        self.in_userinfo = False
        self.in_th = False
        self.in_id = False
        self.got_id = False


        if "brew" in task_url:
            self.ttype = "brew"
        else:
            self.ttype = "koji"

        f = urllib2.urlopen(task_url)
        self.feed(f.read())
        f.close()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                #print attr[0] == "href", attr[1]
                if attr[0] == "href" and "userinfo" in attr[1]:
                    self.in_userinfo = True

        if tag == 'th':
            self.in_th = True

        if tag == 'td' and self.got_id:
            self.in_id = True

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.in_userinfo and self.user is None:
            #print "setting user to: ", data
            self.user = data
            self.in_userinfo = False

        if self.in_th and data == "ID":
            self.got_id = True

        if self.in_id:
            self.in_id = False
            self.got_id = False
            self.tid = data

    def get_rpm_dict(self):
        return self.rpm_dict


# test
if __name__ == "__main__":
    import os
    task = Task("file:///{0}/test.html".format(os.getcwd()))
    print task.ttype, task.user, task.tid

