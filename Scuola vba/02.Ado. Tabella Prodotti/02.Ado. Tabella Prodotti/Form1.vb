Imports System.Data.OleDb



Public Class Form1
    Dim strconnessione As String = "provider=microsoft.jet.oledb.4.0; data source= nw.mdb"
    Dim nmax As Integer = 100
    Dim idcategoria(nmax - 1), n As Integer

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String
        Try
            connessione.ConnectionString = strconnessione
            connessione.Open()
            command.Connection = connessione
            query = "select idcategoria,nomecategoria from categorie"
            command.CommandText = query
            mreader = command.ExecuteReader
            Do While mreader.Read
                cmbcat.Items.Add(mreader("nomecategoria"))
                cmbadd.Items.Add(mreader("nomecategoria"))
                idcategoria(n) = mreader("idcategoria")
                n += 1
            Loop
        Catch
        End Try
        Try
            connessione.Close()

        Catch
        End Try
    End Sub
    Sub dgvuptade(ByVal sql As String)
        Dim connessione As New OleDbConnection
        Dim command As New OleDbCommand
        Dim mreader As OleDbDataReader
        Dim query As String
        Dim r As Integer
        Try
            connessione.ConnectionString = strconnessione
            connessione.Open()
            command.Connection = connessione
            query = sql
            command.CommandText = query
            mreader = command.ExecuteReader
            dgv.Rows.Clear()
            Do While mreader.Read
                dgv.Rows.Add()
                dgv.Rows(r).Cells("IDProdotto").Value = mreader("IDProdotto")
                dgv.Rows(r).Cells("NomeProdotto").Value = mreader("NomeProdotto")
                dgv.Rows(r).Cells("PrezzoUnitario").Value = mreader("PrezzoUnitario")
                dgv.Rows(r).Cells("Scorte").Value = mreader("Scorte")
                dgv.Rows(r).Cells("LivelloDiRiordino").Value = mreader("LivelloDiRiordino")
                r += 1
            Loop
        Catch
        End Try
        Try
            connessione.Close()
        Catch
        End Try

    End Sub
    Private Sub cmbcat_SelectedIndexChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles cmbcat.SelectedIndexChanged
        If lvlriordino.Checked Then
            dgvuptade("select IDProdotto, nomeProdotto, PrezzoUnitario, Scorte, livelloDiRiordino from prodotti as p where p.IDCategoria = " & idcategoria(cmbcat.SelectedIndex) & " and scorte < livelloDiRiordino")
        Else
            dgvuptade("select IDProdotto, nomeProdotto, PrezzoUnitario, Scorte, livelloDiRiordino from prodotti as p where p.IDCategoria = " & idcategoria(cmbcat.SelectedIndex))
        End If
    End Sub

    Private Sub lvlriordino_CheckedChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles lvlriordino.CheckedChanged
        If cmbcat.SelectedIndex <> -1 Then
            If lvlriordino.Checked Then
                dgvuptade("select IDProdotto, nomeProdotto, PrezzoUnitario, Scorte, livelloDiRiordino from prodotti as p where p.IDCategoria = " & idcategoria(cmbcat.SelectedIndex) & " and scorte < livelloDiRiordino")
            Else
                dgvuptade("select IDProdotto, nomeProdotto, PrezzoUnitario, Scorte, livelloDiRiordino from prodotti as p where p.IDCategoria = " & idcategoria(cmbcat.SelectedIndex))
            End If
        End If

    End Sub
    Private Sub txtnomeprodotto_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles txtnomeprodotto.Click
        txtnomeprodotto.Text = ""
    End Sub
    Private Sub txtpu_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles txtpu.Click
        txtpu.Text = ""
    End Sub
    Private Sub txtscorte_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles txtscorte.Click
        txtscorte.Text = ""
    End Sub
    Private Sub txtldo_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles txtldo.Click
        txtldo.Text = ""
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim nomeprodotto As String
        Dim scorte, livellodiriordino As Integer
        Dim pu As Decimal
        Dim ver, idcat As Integer
        
        If IsNumeric(txtldo.Text) Then
            txtldo.ForeColor = Color.Black
            ver += 1
            livellodiriordino = txtldo.Text
        Else
            txtldo.ForeColor = Color.Red
            txtldo.Text = "Livello di Riordino"
        End If

        If IsNumeric(txtscorte.Text) Then
            txtscorte.ForeColor = Color.Black
            ver += 1
            scorte = txtscorte.Text
        Else
            txtscorte.ForeColor = Color.Red
            txtscorte.Text = "Scorte"
        End If
        If txtnomeprodotto.Text <> "" And txtnomeprodotto.Text <> "Nome Prodotto" Then
            txtnomeprodotto.ForeColor = Color.Black
            ver += 1
            nomeprodotto = txtnomeprodotto.Text.Replace("'", "'''")
        Else
            txtnomeprodotto.ForeColor = Color.Red
            txtnomeprodotto.Text = "Nome Prodotto"
        End If
        txtpu.Text = txtpu.Text.Replace(",", ".")
        If IsNumeric(txtpu.Text) Then
            txtpu.ForeColor = Color.Black
            ver += 1
            pu = txtpu.Text
        Else
            txtpu.ForeColor = Color.Red
            txtpu.Text = "Prezzo Unitario"
        End If

        If cmbadd.SelectedIndex <> -1 Then
            cmbadd.ForeColor = Color.Black
            idcat = idcategoria(cmbadd.SelectedIndex)
            ver += 1
        Else
            cmbadd.ForeColor = Color.Red
            cmbadd.Text = "Seleziona una categoria"
        End If
        If ver = 5 Then
            Dim connessione As New OleDbConnection
            Dim command As New OleDbCommand
            Dim query As String
            Try
                connessione.ConnectionString = strconnessione
                connessione.Open()
                command.Connection = connessione
                query = "insert into prodotti (nomeProdotto, PrezzoUnitario, Scorte, livelloDiRiordino, idcategoria) values ('" & nomeprodotto & "' , " & pu & " , " & scorte & " , " & livellodiriordino & " , " & idcat & " )"
                command.CommandText = query
                command.ExecuteNonQuery()
                Button1.BackColor = Color.LightGreen
                MsgBox("AGGIUNTO CORETTAMENTE")
                txtldo.Text = "Livello di Riordino"
                cmbadd.Text = "Seleziona una categoria"
                txtpu.Text = "Prezzo Unitario"
                txtscorte.Text = "Scorte"
                txtnomeprodotto.Text = "Nome Prodotto"
                Button1.BackColor = Color.Transparent
            Catch es As Exception
                MsgBox(es.Message)
            End Try
            Try
                connessione.Close()
            Catch
            End Try

        Else
            Button1.BackColor = Color.Red
        End If
    End Sub
End Class
