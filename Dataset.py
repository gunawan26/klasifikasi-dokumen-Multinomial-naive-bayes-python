import SqlConnector


class Dataset:
    connect = SqlConnector.sql_connect()
    cursor = connect.cursor()


    def insert_training(self,title_args,abstract_args,id_kat):
        q = "INSERT INTO tb_training(title,abstract,id_kategori) VALUES('{0}','{1}',{2})".format(title_args,abstract_args,id_kat)
        print(q)
        self.cursor.execute(q)
        self.connect.commit()


        return True


    def set_kat(self,kat_args):
        q = "SELECT MAX(id_kategori) FROM tb_kategori WHERE nama_kategori = '{0}'".format(kat_args)
        self.cursor.execute(q)
        val = self.cursor.fetchone()

        get_id = val[0]
        if get_id is None:
            qInsert = "INSERT INTO tb_kategori VALUES(NULL,'{0}')".format(kat_args)
            self.cursor.execute(qInsert)
            self.connect.commit()

        self.cursor.execute(q)
        val = self.cursor.fetchone()

        return val[0]


    def get_training(self):
        q = "SELECT tb_kategori.nama_kategori,abstract FROM tb_training inner join tb_kategori using (id_kategori)"
        self.cursor.execute(q)
        val = self.cursor.fetchall()
        return val


    def combo_text(self):
        q = "SELECT nama_kategori FROM tb_kategori"
        self.cursor.execute(q)
        val = self.cursor.fetchall()
        my_val = (list(x[0] for x in val))
        return my_val


    def count_kategori(self):

        q="SELECT tb_kategori.`nama_kategori`, COUNT(id_kategori) AS jumlah FROM tb_training INNER JOIN tb_kategori USING (id_kategori) GROUP BY id_kategori"
        self.cursor.execute(q)
        val = self.cursor.fetchall()

        return val





