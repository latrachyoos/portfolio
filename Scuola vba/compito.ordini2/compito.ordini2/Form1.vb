Public Class Form1

    Private Sub Form1_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        dgv.Rows.Clear()
        carica()
    End Sub

    Structure stcOrdine
        Dim IDOrdine As Integer
        <VBFixedString(40)> Dim NomeProdotto As String
        Dim PrezzoUnitaro As Decimal
        Dim Scorte As Integer
        <VBFixedString(30)> Dim Nomecategoria As String
    End Structure

    Dim File As String = "prodotti.csv"
    Dim Lrec As Integer
    Dim Nmax As Integer = 100
    Dim M(Nmax) As stcOrdine
    Dim N As Integer
    Sub carica()
        Dim S() As String
        Dim O As stcOrdine
        Try
            Kill("ordini.rnd")
        Catch ex As Exception
        End Try

        Lrec = Len(O)
        FileOpen(1, File, OpenMode.Input)
        FileOpen(2, "ordini.rnd", OpenMode.Random, , , Lrec)
        Do While Not EOF(1)
            S = Split(LineInput(1), ";")
            O.IDOrdine = S(0)
            O.NomeProdotto = S(1)
            O.PrezzoUnitaro = S(2)
            O.Scorte = S(3)
            O.Nomecategoria = S(4)
            FilePut(2, O, N + 1)
            N += 1
        Loop
        FileClose(1)
        FileClose(2)
        importo()
    End Sub

    Sub importo()
        FileOpen(2, "ordini.rnd", OpenMode.Random, , , Lrec)
        For i = 1 To LOF(2) \ Lrec
            FileGet(2, M(i - 1), i)
        Next
        FileClose(2)
        caric()
    End Sub

    Sub caric()
        For i = 0 To N - 1
            dgv.Rows.Add()
            dgv.Rows(i).Cells("ID").Value = M(i).IDOrdine
            dgv.Rows(i).Cells("Nome").Value = M(i).NomeProdotto
            dgv.Rows(i).Cells("Prezzo").Value = M(i).PrezzoUnitaro
            dgv.Rows(i).Cells("Scorte").Value = M(i).Scorte
            dgv.Rows(i).Cells("Categoria").Value = M(i).Nomecategoria
            cari(M(i).Nomecategoria)
        Next
    End Sub

    Sub cari(ByVal Cat As String)
        Dim add As Boolean = True
        Dim Nu As Integer = ComboBox1.Items.Count
        Dim i As Integer
        If Nu > 0 Then
            Do
                If Cat = ComboBox1.Items(i) Then
                    add = False
                End If
                i += 1
            Loop Until Not add Or i > Nu - 1
        End If
        If add Then
            ComboBox1.Items.Add(Cat)
        End If
    End Sub

    Sub car()
        Dim R As stcOrdine
        dgv.Rows.Clear()
        FileOpen(1, "ordini.rnd", OpenMode.Random, , , Lrec)
        For i = 1 To LOF(1) \ Lrec
            FileGet(1, R, i)
            If R.Nomecategoria = ComboBox1.Text Then
                ca(R)
            End If
        Next
        FileClose(1)
    End Sub

    Private Sub ca(ByRef R As stcOrdine)
        Dim i As Integer = dgv.Rows.Count
        dgv.Rows.Add()
        dgv.Rows(i).Cells("ID").Value = R.IDOrdine
        dgv.Rows(i).Cells("Nome").Value = R.NomeProdotto
        dgv.Rows(i).Cells("Prezzo").Value = R.PrezzoUnitaro
        dgv.Rows(i).Cells("Scorte").Value = R.Scorte
        dgv.Rows(i).Cells("Categoria").Value = R.Nomecategoria
    End Sub

    Sub MinScorte(ByVal Sco As Integer)
        dgv.Rows.Clear()
        For i = 0 To N - 1
            If M(i).Scorte < Sco Then
                ca(M(i))
            End If
        Next
    End Sub

    Sub Sigla(ByVal Sig As String)
        dgv.Rows.Clear()
        For i = 0 To N - 1
            If LCase(Mid(M(i).NomeProdotto, 1, Len(Sig))) = LCase(Sig) Then
                ca(M(i))
            End If
        Next
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        car()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        If IsNumeric(TextBox1.Text) Then
            MinScorte(Trim(TextBox1.Text))
        End If
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        If Trim(TextBox1.Text) <> "" Then
            Sigla(Trim(TextBox1.Text))
        End If
    End Sub
End Class
'Importare in un file random i dati presenti nel file CSV
'Caricare in un array di record i dati presenti nel file random
'Visualizzare i dati dell'array di record in una datagridview
'Visualizzare i prodotti le cui scorte sono inferiori ad un numero inserito in una textbox
'Visualizzare i prodotti il cui nome inizia con una sigla inserita dall'utente
'Inserire in una combobox tutte le categorie presenti (senza ripetizioni)
'Visualizzare i prodotti di una categoria selezionata dalla combobox.